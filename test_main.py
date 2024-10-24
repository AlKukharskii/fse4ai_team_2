import unittest
import os
from unittest import mock
from unittest.mock import patch
import main

class TestMainFunction(unittest.TestCase):

    @patch('main.MobileNetV2')
    @patch('main.preprocess_image')
    @patch('main.open', new_callable=mock.mock_open)
    def test_main_function_runs(self, mock_open_file, mock_preprocess_image, mock_model_class):
        mock_model = mock_model_class.return_value
        mock_model.load_state_dict.return_value = None
        mock_model.eval.return_value = None
        mock_model.float.return_value = None

        mock_preprocess_image.return_value = mock.MagicMock()

        main.main('/input_raw/resized_image.jpg', '/output/output_prediction.txt')

        mock_model.load_state_dict.assert_called()
        mock_model.eval.assert_called()

    def test_missing_input_image(self):
        # Test with a missing input image
        with self.assertRaises(FileNotFoundError):
            main.preprocess_image('/nonexistent/image.jpg')

    @patch('main.open', new_callable=mock.mock_open)
    def test_output_file_created(self, mock_file):
        with patch('main.preprocess_image'), \
             patch('main.MobileNetV2'), \
             patch('main.IMAGENET_CATEGORIES', {0: 'class0'}):
            main.main('/input_raw/resized_image.jpg', '/output/output_prediction.txt')
            mock_file.assert_called_with('/output/output_prediction.txt', 'w')

    @patch('main.MobileNetV2')
    @patch('main.preprocess_image')
    @patch('main.open', new_callable=mock.mock_open)
    def test_model_weights_missing(self, mock_open_file, mock_preprocess_image, mock_model_class):
        # Simulate FileNotFoundError when loading model weights
        mock_model = mock_model_class.return_value
        mock_model.load_state_dict.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            main.main('/input_raw/resized_image.jpg', '/output/output_prediction.txt')

    def test_prediction_output(self):
        # Mock functions to control the output
        with patch('main.preprocess_image'), \
             patch('main.MobileNetV2') as mock_model_class, \
             patch('main.open', new_callable=mock.mock_open()) as mock_file, \
             patch('main.IMAGENET_CATEGORIES', {0: 'class0'}):
            mock_model = mock_model_class.return_value
            mock_model.load_state_dict.return_value = None
            mock_model.eval.return_value = None
            mock_model.float.return_value = None
            mock_output = mock.MagicMock()
            mock_output.max.return_value = (None, mock.Mock(item=lambda: 0))
            mock_model.__call__.return_value = mock_output

            main.main('/input_raw/resized_image.jpg', '/output/output_prediction.txt')

            # Check that the output file was written with the expected content
            mock_file().write.assert_called_with('Predicted class label: class0\n')

if __name__ == '__main__':
    unittest.main()