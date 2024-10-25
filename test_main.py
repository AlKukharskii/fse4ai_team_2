import unittest
import sys
sys.path.append("/usr/src/app/model")
from unittest import mock
from unittest.mock import patch
from main import main
from nets import MobileNetV2
import torch

class TestMainFunction(unittest.TestCase):

    def test_missing_input_image(self):
        # Test with a missing input image
        with self.assertRaises(FileNotFoundError):
            main().preprocess_image('/nonexistent/image.jpg')

    # def test_tensor_size(self):
    #     image, img_shape, img_type = main().preprocess_image('/input/resized_image.jpg')
    #     print(img_shape, img_type)
    #     self.assertEqual(img_shape, (1,2,3), 'Not Equal Shape')
    #
    # def test_image_type(self):
    #     image, img_shape, img_type = main().preprocess_image('/input/resized_image.jpg')
    #     print(img_shape, img_type)
    #     self.assertEqual(img_type, int, 'Not Equal Image Type')
    #
    # def test_image_class(self):
    #     model = MobileNetV2()
    #     model.load_state_dict(torch.load("./model/weights/mobilenetv2.pt", weights_only=True))  # weights ported from torchvision
    #     model.float()
    #
    #     predicted_label = main().inference(model, '/input/resized_image.jpg',
    #                      '/output_raw/output_prediction.txt')
    #
    #     print('Label in output:',predicted_label)
    #     self.assertEqual(predicted_label, 'Aar', 'Wrong classification')

if __name__ == '__main__':
    unittest.main()
