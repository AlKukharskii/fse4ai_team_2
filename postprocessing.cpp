// Input class name over a figure 
#include <iostream> 
#include <opencv2/core/core.hpp> 

#include <opencv2/highgui/highgui.hpp> 
#include <opencv2/imgproc.hpp> 

#include <string>
#include <fstream>

using namespace cv; 
using namespace std; 

// Driver Code 
int main(int argc, char** argv) 
{ 
	 
	Mat image = imread("resized_image.jpg",IMREAD_COLOR); 

	// Check if the image is 
	// created successfully. 
	if (!image.data) { 
		cout << "Could not open or"
			<< " find the image" << std::endl; 
		return 0; 
	} 

	// Read class name
	ifstream myfile;
	myfile.open("output_prediction.txt");
	string myline;
	getline (myfile, myline);

	// Writing over the Image 
	Point org(1, 30); 
	putText(image, myline, org, 
			FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, 
			Scalar(51, 153, 255), 1, LINE_AA);

	imwrite("image_with_label.jpg", image);	

	return 0; 
} 

