#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <string>
#include <fstream>
#include <filesystem> 

using namespace cv;
using namespace std;
namespace fs = std::filesystem; 

int main(int argc, char** argv) {
    // Paths to input, output_raw, and output directories
    string input_dir = "input/resized_image.jpg";
    string output_raw_file = "output_raw/output_prediction.txt";
    string output_image = "output/image_with_label.jpg";

    // Load the image from the input directory
    Mat image = imread(input_dir, IMREAD_COLOR);

    // Check if the image was loaded successfully
    if (image.empty()) {
        cerr << "Error: Could not open or find the image!" << endl;
        return 1;
    }

    // Open the prediction text file from the output_raw directory
    ifstream myfile(output_raw_file);
    if (!myfile.is_open()) {
        cerr << "Error: Could not open prediction file!" << endl;
        return 1;
    }

    // Read the prediction from the text file
    string prediction;
    getline(myfile, prediction);
    myfile.close();

    // Add the prediction as a label on the image
    Point org(1, 30);  // Text position on the image
    putText(image, prediction, org, FONT_HERSHEY_SIMPLEX, 1.0,
            Scalar(51, 153, 255), 2, LINE_AA);

    // Ensure the output directory exists
    fs::create_directory("output");

    // Save the labeled image in the output directory
    imwrite(output_image, image);
    cout << "Image with label saved at: " << output_image << endl;

    // Remove input and output_raw directories
    try {
        fs::remove_all("input");
        fs::remove_all("output_raw");
        cout << "Directories 'input' and 'output_raw' removed." << endl;
    } catch (const fs::filesystem_error& e) {
        cerr << "Error deleting directories: " << e.what() << endl;
        return 1;
    }

    return 0;
}
 

