#!/bin/bash

gcc postprocessing.cpp `pkg-config --cflags --libs opencv4` -std=c++11 -lstdc++ -o postprocessing.out

