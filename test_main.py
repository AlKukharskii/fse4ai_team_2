import unittest
import sys
import os
sys.path.append("/usr/src/app/model")
from unittest import mock
from unittest.mock import patch
import main
from nets import MobileNetV2
import torch

class TestMainFunction(unittest.TestCase):

    def __init__(self):
        self.input_dir = "input_raw"
        self.resized_image_path = os.path.join(self.input_dir, "image.jpg")
        self.output_dir = "output_raw"
        os.makedirs(self.output_dir, exist_ok=True)  # Create output_raw if it doesn't exist
        self.output_file_path = os.path.join(self.output_dir, "output_prediction.txt")

    def test_missing_input_image(self):
        # Test with a missing input image
        with self.assertRaises(FileNotFoundError):
            main.preprocess_image('/nonexistent/image.jpg')

    def test_tensor_size(self):
        image, img_shape, img_type = main.preprocess_image(self.resized_image_path)
        print(img_shape, img_type)
        self.assertNotEqual(img_shape, (1,2,3), 'Equal Shape')

    def test_image_type(self):
        image, img_shape, img_type = main.preprocess_image(self.resized_image_path)
        print(img_shape, img_type)
        self.assertNotEqual(img_type, int, 'Equal Image Type')

    def test_image_class(self):
        model = MobileNetV2()
        model.load_state_dict(torch.load("/Users/aibekakhmetkazy/PycharmProjects/fse4ai_team_2/mobilenetv2-pytorch/weights/mobilenetv2.pt", weights_only=True))  # weights ported from torchvision
        model.float()

        predicted_label = main.inference(model, self.resized_image_path,
                         self.output_file_path)

        print('Label in output:',predicted_label)
        self.assertNotEqual(predicted_label, 'House', 'Correct classification')

if __name__ == '__main__':
    unittest.main()
