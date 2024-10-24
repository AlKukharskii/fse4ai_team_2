# Load base image (it should support both Python and C++)
FROM nvidia/cuda:12.0.0-devel-ubuntu20.04

# Set timezone environment variables to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC

# Copy the Makefile and all necessary C++ files into the working directory
COPY Makefile /app/Makefile
COPY Makefile.run /app/Makefile.run
COPY preprocessing.cpp /app/preprocessing.cpp
COPY postprocessing.cpp /app/postprocessing.cpp
COPY main.py /app/main.py
COPY test_main.py /app/test_main.py

# Set the working directory
WORKDIR /app

# Install any project-specific dependencies and compile C++ components
RUN make

# Clone repository
RUN git clone https://github.com/yakhyo/mobilenetv2-pytorch.git /usr/src/app/model

# Set the working directory
WORKDIR /app/model

# Install Python dependencies from requirements.txt
RUN pip3 install -r requirements.txt

# Set the working directory
WORKDIR /app

# Run the tests to ensure everything is working correctly
RUN make test

# Set the entrypoint to run the pipeline via Makefile.run
ENTRYPOINT ["make", "-f", "Makefile.run"]

# Default command to run the pipeline with default input/output paths
CMD ["run", "INPUT_DIR=input_raw"]
