# Variables for paths
SRC_DIR := /usr/src/mobilenetv2
BUILD_DIR := /usr/src/app
PYTHON_REQS := requirements.txt

# Default target: Install prerequisites and build everything
all: build

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
	git clone https://github.com/yakhyo/mobilenetv2-pytorch.git $(SRC_DIR)
	cd $(SRC_DIR) && pip3 install -r $(PYTHON_REQS)

# Target to build C++ executables for preprocessing and postprocessing
build:
	@echo "Building C++ executables..."
	gcc preprocessing.cpp `pkg-config --cflags --libs opencv4` -std=c++17 -lstdc++ -o preprocessing.out
	gcc postprocessing.cpp `pkg-config --cflags --libs opencv4` -std=c++17 -lstdc++ -o postprocessing.out


# Clean target to remove built files or unnecessary directories
clean:
	@echo "Cleaning up..."
	rm -f preprocessing.out postprocessing.out

# Add test target 
test:
	@echo "Running tests..."

