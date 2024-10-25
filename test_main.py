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

    input_dir = "input_raw"
    resized_image_path = os.path.join(input_dir, "image.jpg")
    output_dir = "output_raw"
    os.makedirs(output_dir, exist_ok=True)  # Create output_raw if it doesn't exist
    output_file_path = os.path.join(output_dir, "output_prediction.txt")

    def test_missing_input_image(self):
        # Test with a missing input image
        with self.assertRaises(FileNotFoundError):
            main.preprocess_image('/nonexistent/image.jpg')

    def test_tensor_size(self, resized_image_path):
        image, img_shape, img_type = main.preprocess_image(resized_image_path)
        print(img_shape, img_type)
        self.assertNotEqual(img_shape, (1,2,3), 'Equal Shape')

    def test_image_type(self, resized_image_path):
        image, img_shape, img_type = main.preprocess_image(resized_image_path)
        print(img_shape, img_type)
        self.assertNotEqual(img_type, int, 'Equal Image Type')

    def test_image_class(self, resized_image_path, output_file_path):
        model = MobileNetV2()
        model.load_state_dict(torch.load(".model/weights/mobilenetv2.pt", weights_only=True))  # weights ported from torchvision
        model.float()

        predicted_label = main.inference(model, resized_image_path,
                         output_file_path)

        print('Label in output:',predicted_label)
        self.assertNotEqual(predicted_label, 'House', 'Correct classification')

if __name__ == '__main__':
    unittest.main()
