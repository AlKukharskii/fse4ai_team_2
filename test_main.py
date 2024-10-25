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
        print('Test1 on Nonexisting image')
        with self.assertRaises(FileNotFoundError):
            main.preprocess_image('/nonexistent/image.jpg')

    def test_tensor_size(self):
        input_dir = "input_raw"
        resized_image_path = os.path.join(input_dir, "image.jpg")
        image, img_shape, img_type = main.preprocess_image(resized_image_path)
        print('Test2 on Tensor Size')
        print(len(img_shape))
        self.assertNotEqual(img_shape, torch.Size([1, 3, 3031, 5184]), 'Not equal Shape')

    def test_image_type(self):
        input_dir = "input_raw"
        resized_image_path = os.path.join(input_dir, "image.jpg")
        image, img_shape, img_type = main.preprocess_image(resized_image_path)
        print('Test3 on Image Type')
        print(img_type, str(img_type))
        self.assertEqual(img_type, "<class 'torch.Tensor'>", 'Equal Image Type')

if __name__ == '__main__':
    unittest.main()
