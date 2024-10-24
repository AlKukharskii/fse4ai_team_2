# Multiclass Image Classification with MobileNet-V2

## Project Description
This project implements a multiclass image classification pipeline using a pretrained MobileNet-V2 neural network model. The pipeline includes preprocessing, processing, and postprocessing steps, all orchestrated using Makefiles and Docker for ease of deployment and reproducibility.

## Team
- Aibek Akhmetkazy
- Hassan Iftikhar
- Aleksandr Kukharskii
- Rinat Prochii

## Getting Started

### Prerequisites
- Docker
- NVIDIA GPU with CUDA (for processing)

### Installation and Setup
1. Clone the Repository:
   ```bash
   git clone https://github.com/AlKukharskii/fse4ai_team_2.git
   cd fse4ai_team_2
   ```

2. Build the Docker Image:
   ```bash
   docker build -t image-classification .
   ```

3. Run Makefile Targets:
   Install dependencies and compile necessary components:
   ```bash
   docker run --rm image-classification make prereqs
   docker run --rm image-classification make build
   ```

### Testing the Setup
Verify that all system components function correctly:
```bash
docker run --rm image-classification make test
```

## Usage

### Docker Container Execution
Execute the project within Docker, automating the full workflow from preprocessing to postprocessing:

1. **Preprocessing**: Prepare images for classification
   ```bash
   docker run --rm -v $(pwd)/input_raw:/input_raw -v $(pwd)/input:/input image-classification make preprocess
   ```

2. **Processing**: Classify images using MobileNet-V2
   ```bash
   docker run --rm -v $(pwd)/input:/input -v $(pwd)/output_raw:/output_raw image-classification make process
   ```

3. **Postprocessing**: Annotate and save images with their predicted labels
   ```bash
   docker run --rm -v $(pwd)/output_raw:/output_raw -v $(pwd)/output:/output image-classification make postprocess
   ```

Alternatively, you can execute the entire pipeline using the default command:
```bash
docker run --rm -v $(pwd)/input_raw:/input_raw -v $(pwd)/output:/output image-classification
```

## Makefile Details
The project provides two Makefiles:

### Makefile (Build System)
This Makefile is used to compile all binary executables and/or libraries necessary for the project. The Dockerfile relies on this Makefile to build the project inside a Docker image. It includes the following targets:

- **prereqs**: Installs all dependencies, compiles, and installs necessary components.
- **build**: Compiles all necessary executables, including preprocessing (`preprocessing.out`) and postprocessing (`postprocessing.out`) executables.
- **test**: Tests all steps of the pipeline, including verifying the correctness of preprocessing, processing, and postprocessing.

### Makefile.run (Entry Point for Docker Image)
This Makefile serves as an entry point for running the pipeline in the Docker container. It orchestrates the following steps:

- **preprocess**: Converts all files in `/input_raw` to a standardized format in `/input`.
- **process**: Uses the neural network model to classify images from `/input` and writes results to `/output_raw`.
- **postprocess**: Annotates images using results from `/output_raw` and saves them in `/output`.

## Example Input and Output
- **Input**: The input is a raw image (`image.jpg`), which is first downscaled to `224x224` pixels in the preprocessing step.
- **Output**: The processed output consists of the predicted class label saved in `output_prediction.txt`, and the postprocessed output is the annotated image (`image_with_label.jpg`).

## GitHub Actions Workflow
The repository includes a GitHub Actions workflow that automates the building and testing of the Docker image. This ensures that all commits and pull requests pass the `make prereqs`, `make build`, and `make test` stages.

## Acknowledgments
Acknowledgments to data sources, libraries, and frameworks used in this project, such as:
- MobileNet-V2 for the pretrained model architecture.
- Docker for containerization, ensuring a consistent runtime environment.
- TensorFlow for model implementation and training.
- OpenCV for image preprocessing and handling.
- NVIDIA for providing CUDA and GPU support for accelerated processing.
- Ubuntu 20.04 as the base environment for building the project.
- GNU Make for orchestrating the build, test, and run processes.
- GitHub Actions for providing CI/CD for building and testing the project.
- Contributors of the project: Aibek Akhmetkazy, Hassan Iftikhar, Aleksandr Kukharskii, Rinat Prochii.
