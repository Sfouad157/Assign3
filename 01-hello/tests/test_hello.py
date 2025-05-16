import subprocess
import unittest

class TestPrintOutput(unittest.TestCase):
    def test_output(self):
        # Run the script and capture output
        result = subprocess.run(['python', '01-hello/hello.py'], text=True, capture_output=True)
        # Check the output
        self.assertEqual(result.stdout.strip(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()