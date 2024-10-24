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
            f.write(f"Predicted class label: {predicted_label}\n")

    # Input directory
    input_dir = "input"
    resized_image_path = os.path.join(input_dir, "resized_image.jpg")
    
    # Output directory
    output_dir = "output_raw"
    os.makedirs(output_dir, exist_ok=True)  # Create output_raw if it doesn't exist
    output_file_path = os.path.join(output_dir, "output_prediction.txt")
    
    # Call the inference function
    inference(model, resized_image_path, output_file_path)

if __name__ == "__main__":
    main(input_path, output_path)
