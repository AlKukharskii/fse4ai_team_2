# Load base image (it should support both Python and C++)
FROM nvidia/cuda:12.0.0-devel-ubuntu20.04

# Set timezone environment variables to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC

# Install general dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    libopencv-dev \
    && apt-get clean
# Install Python3 and pip
RUN apt-get install -y python3 python3-pip
# Clone the MobileNetV2 repository
RUN git clone https://github.com/yakhyo/mobilenetv2-pytorch.git /usr/src/mobilenetv2
WORKDIR /usr/src/mobilenetv2
# Install Python dependencies from requirements.txt
RUN pip3 install -r requirements.txt

# Copy the Makefile and all necessary C++ files into the working directory
COPY Makefile /usr/src/app/Makefile
COPY Makefile.run /usr/src/app/Makefile.run
COPY preprocessing.cpp /usr/src/app/preprocessing.cpp
COPY postprocessing.cpp /usr/src/app/postprocessing.cpp
COPY main.py /usr/src/app/main.py

# Set the working directory
WORKDIR /usr/src/app

# Install any project-specific dependencies and compile C++ components
RUN make

# Run the tests to ensure everything is working correctly
RUN make test

# Set the entrypoint to run the pipeline via Makefile.run
ENTRYPOINT ["make", "-f", "Makefile.run"]

# Default command to run the pipeline with default input/output paths
CMD ["run", "INPUT_DIR=/input_raw"]
