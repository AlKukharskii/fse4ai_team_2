#!/bin/bash

gcc preprocessing.cpp `pkg-config --cflags --libs opencv4` -std=c++11 -lstdc++ -o preprocessing.out

