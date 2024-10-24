import os
import torch
from torchvision import transforms
from PIL import Image
from nets import MobileNetV2
from assets.meta import IMAGENET_CATEGORIES

def main(resized_image_path, output_file_path):
    model = MobileNetV2()
    model.load_state_dict("./weights/mobilenetv2.pt")  # weights ported from torchvision
    model.float()  # converting weights to float32

    # Assume the image is already resized; no need for transforms.Resize
    def preprocess_image(resized_image_path):
        transform = transforms.Compose([
            transforms.ToTensor(),  # Convert the image to a PyTorch tensor
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],  # Normalize using the mean and std of ImageNet
                std=[0.229, 0.224, 0.225]
            ),
        ])

        image = Image.open(resized_image_path)
        image = transform(image).unsqueeze(0)  # Add a batch dimension
        return image

    def inference(model, resized_image_path, output_file_path):
        model.eval()

        input_image = preprocess_image(resized_image_path)
        with torch.no_grad():
            output = model(input_image)

        _, predicted_class = output.max(1)
        predicted_label = IMAGENET_CATEGORIES[predicted_class.item()]

        # Write output in text file
        with open(output_file_path, "w") as f:
          # f.write(f"Predicted class index: {predicted_class.item()}\n")
            f.write(f"Predicted class label: {predicted_label}\n")

    # Call the inference function
    inference(model, resized_image_path, output_file_path)

if __name__ == "__main__":
    # Retrieve input and output paths from environment variables
    input_path = os.getenv('INPUT_DIR', '/input_raw/resized_image.jpg')
    output_path = os.getenv('OUTPUT_DIR', '/output/output_prediction.txt')

    # Run the main function with the retrieved paths
    main(input_path, output_path)
