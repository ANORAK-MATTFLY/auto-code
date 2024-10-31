import unittest
import os
import json
from file_processing.file_handling import process_file, save_to_json, process_directory  # Import from your actual module
from unittest.mock import patch, MagicMock
from tempfile import TemporaryDirectory
from pathlib import Path

class TestFileProcessingFunctions(unittest.TestCase):

    def test_process_file_typical_case(self):
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test_file.txt"
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("Hello, World!")
            content = process_file(str(file_path))
            self.assertEqual(content, "Hello, World!")

    def test_process_file_non_existent_file(self):
        non_existent_path = "/path/that/does/not/exist.txt"
        content = process_file(non_existent_path)
        self.assertIsNone(content)

    def test_process_file_permission_error(self):
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test_file.txt"
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("Hello, World!")
            # Simulate permission error by changing file permissions
            import stat
            file_path.chmod(stat.S_IRUSR)  # Only readable by owner
            # Test as non-owner (simulation, actual test might require running as different user)
            with patch('builtins.open', side_effect=PermissionError()):
                content = process_file(str(file_path))
                self.assertIsNone(content)

    def test_save_to_json_typical_case(self):
        data = {"key": "value"}
        filename = "test_save.json"
        save_to_json(data, filename)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r', encoding='utf-8') as json_file:
            loaded_data = json.load(json_file)
            self.assertEqual(data, loaded_data)
        os.remove(filename)  # Cleanup

    def test_save_to_json_error_handling(self):
        data = {"key": "value"}
        filename = "/path/that/does/not/exist/test_save.json"  # Assuming this path is not writable
        # Simulate write error
        with patch('builtins.open', side_effect=IOError()):
            save_to_json(data, filename)

    @patch('file_processing.process_file')
    def test_process_directory_typical_case(self, mock_process_file):
        mock_process_file.return_value = "Mocked Content"
        with TemporaryDirectory() as tmp_dir:
            # Create test directory structure
            Path(tmp_dir) / "test_file.py".touch()
            result = process_directory(tmp_dir)
            self.assertIn(str(Path(tmp_dir) / "test_file.py"), result)
            self.assertEqual(result[str(Path(tmp_dir) / "test_file.py")]["content"], "Mocked Content")

    def test_process_directory_non_existent_dir(self):
        non_existent_dir = "/path/that/does/not/exist"
        result = process_directory(non_existent_dir)
        self.assertEqual(result, {})

    def test_process_directory_ignores_pytest_cache(self):
        with TemporaryDirectory() as tmp_dir:
            (Path(tmp_dir) / ".pytest_cache" / "test_file.py").parent.mkdir(parents=True, exist_ok=True)
            (Path(tmp_dir) / ".pytest_cache" / "test_file.py").touch()
            (Path(tmp_dir) / "test_file.py").touch()
            with patch('file_processing.process_file') as mock_process_file:
                mock_process_file.return_value = "Mocked Content"
                result = process_directory(tmp_dir)
                # Only non-.pytest_cache file should be processed
                self.assertEqual(len(result), 1)
                self.assertIn(str(Path(tmp_dir) / "test_file.py"), result)

if __name__ == '__main__':
    unittest.main()
