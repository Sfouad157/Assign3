import unittest
from unittest.mock import patch
from io import StringIO
import sys

file = "04-tip/tip.py"
test_params = [
    (['100', '15'], "A 15% tip on $100.0 is $15.0"),
    (['45.62', '20'], "A 20% tip on $45.62 is $9.124")
]

class TestTipCalculation(unittest.TestCase):

    @patch('builtins.input', create=True)  # Mocking inputs
    def test_tip_output(self, mock_input):
        for params in test_params:
            test_input = params[0]
            expected_output = params[1].strip()
            mock_input.side_effect = test_input

            # Redirect stdout to capture prints
            captured_output = StringIO()
            sys.stdout = captured_output
            
            # Execute script
            exec(open(file).read())
            
            sys.stdout = sys.__stdout__
            
            # Get the output and strip any extra newlines or spaces
            output = captured_output.getvalue().strip()
            
            # Check if the output is the expected string
            self.assertEqual(output, expected_output, f"For input {test_input}, I expected '{expected_output}', but got '{output}'")

if __name__ == '__main__':
    unittest.main()
