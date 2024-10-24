#!/bin/bash

gcc resize_image.cpp `pkg-config --cflags --libs opencv4` -std=c++11 -lstdc++ -o resize.out

