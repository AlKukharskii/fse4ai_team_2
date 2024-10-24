#include <opencv2/opencv.hpp>
#include <iostream>
#include <filesystem>
#include <string>

using namespace std;
using namespace cv;
namespace fs = std::filesystem;

int main(int argc, char** argv) {
    // Check if the --input flag is provided with a directory path
    if (argc < 3 || string(argv[1]) != "--input") {
        cerr << "Usage: ./preprocessing.out --input <directory_path>" << endl;
        return 1;
    }

    // Get the directory path from the command-line argument
    string input_dir = argv[2];

    // Construct the full path to the input image (image.jpg)
    string image_path = input_dir + "/image.jpg";
    cout << "Processing: " << image_path << endl;

    // Load the image from the constructed path
    Mat image = imread(image_path, IMREAD_COLOR);
    if (image.empty()) {
        cerr << "Error: Could not open or find the image at " << image_path << endl;
        return 1;
    }

    // Resize the image to 224x224
    Mat resized_image;
    resize(image, resized_image, Size(224, 224), INTER_LINEAR);

    // Save the resized image as resized_image.jpg in the same directory
    string output_path = input_dir + "/resized_image.jpg";
    imwrite(output_path, resized_image);

    cout << "Saved resized image to: " << output_path << endl;

    return 0;
}

