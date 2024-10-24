# Load base image (it should support both Python and C++)
FROM nvidia/cuda:12.0-devel-ubuntu20.04

# Install general dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    libopencv-dev \
    && apt-get clean

# Copy the primary Makefile for building and testing
COPY Makefile /usr/src/app/Makefile

# Copy the entry point Makefile for running the pipeline
COPY Makefile.run /usr/src/app/Makefile.run

# Set the working directory
WORKDIR /usr/src/app

# Install any project-specific dependencies and compile C++ components
RUN make prereqs
RUN make build

# Run the tests to ensure everything is working correctly
RUN make test

# Set the entrypoint to run the pipeline via Makefile.run
ENTRYPOINT ["make", "-f", "Makefile.run"]

# Default command to run the pipeline with default input/output paths
CMD ["run", "INPUT_DIR=/input_raw", "OUTPUT_DIR=/output"]
