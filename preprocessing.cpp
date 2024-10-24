// let's start with including libraries 
#include<opencv2/opencv.hpp>
#include<iostream>
 
// Namespace to nullify use of cv::function(); syntax
using namespace std;
using namespace cv;
 
int main()
{
 // Read the image using imread function
 Mat image = imread("image.jpg");
 
 // let's downscale the image using new  width and height
 int down_width = 224;
 int down_height = 224;
 Mat resized_down;

 //resize down
 resize(image, resized_down, Size(down_width, down_height), INTER_LINEAR);

 imwrite("resized_image.jpg", resized_down);

 return 0;
}


