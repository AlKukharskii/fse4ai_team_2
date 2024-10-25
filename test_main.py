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

    def test_missing_input_image(self):
        # Test with a missing input image
        with self.assertRaises(FileNotFoundError):
            main.preprocess_image('/nonexistent/image.jpg')

    def test_tensor_size(self):
        input_dir = "input_raw"
        resized_image_path = os.path.join(input_dir, "image.jpg")
        image, img_shape, img_type = main.preprocess_image(resized_image_path)
        print(img_shape, img_type)
        self.assertNotEqual(img_shape, (1,2,3), 'Equal Shape')

    def test_image_type(self):
        input_dir = "input_raw"
        resized_image_path = os.path.join(input_dir, "image.jpg")
        image, img_shape, img_type = main.preprocess_image(resized_image_path)
        print(img_shape, img_type)
        self.assertNotEqual(img_type, int, 'Equal Image Type')

if __name__ == '__main__':
    unittest.main()
