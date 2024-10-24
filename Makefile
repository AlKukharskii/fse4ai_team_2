# Variables for paths
BUILD_DIR := /usr/src/app
PYTHON_REQS := requirements.txt

# Default target: Install prerequisites, build everything and test
all: prereqs build

# Target to install all prerequisites
prereqs:
	@echo "Installing prerequisites..."
	apt-get update && apt-get install -y \
		build-essential \
		cmake \
		git \
		wget \
		curl \
		libopencv-dev \
		python3 \
		python3-pip && \
		apt-get clean
	ln -s /usr/bin/python3 /usr/bin/python

# Target to build C++ executables for preprocessing and postprocessing
build:
	@echo "Building C++ executables..."
	gcc preprocessing.cpp `pkg-config --cflags --libs opencv4` -std=c++17 -lstdc++ -o preprocessing.out
	gcc postprocessing.cpp `pkg-config --cflags --libs opencv4` -std=c++17 -lstdc++ -o postprocessing.out

# Add test target 
test:
	@echo "Running tests..."
	python -m unittest test_main.py

# Clean target to remove built files or unnecessary directories
clean:
	@echo "Cleaning up..."
	rm -f preprocessing.out postprocessing.out