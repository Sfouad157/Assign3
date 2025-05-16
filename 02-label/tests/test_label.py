import unittest
from unittest.mock import patch
from io import StringIO
from textwrap import dedent
import sys

file = "02-label/label.py"
test_params = [
    (
        ['Mark','McManus','Manager'],
        '''
        McManus, Mark
        Manager
        '''
    ),
    (
        ['Patricia','Peacock','President'],
        '''
        Peacock, Patricia
        President
        '''
    )
]

class TestLabelFormat(unittest.TestCase):
    @patch('builtins.input', create=True)
    def test_output(self, mock_input):

        for params in test_params:
            test_input = params[0]
            expected_output = dedent(params[1]).strip()
            mock_input.side_effect = test_input

            # Redirect stdout to capture prints
            captured_output = StringIO()
            sys.stdout = captured_output
            
            # Execute script
            exec(open(file).read())
            sys.stdout = sys.__stdout__
            
            # Get the output 
            output = captured_output.getvalue().strip()
            
            # Check if the output is lowercase
            self.assertEqual(output, expected_output, f"For values {test_input}, I expected:\n{expected_output}\nbut got:\n{output}")

if __name__ == '__main__':
    unittest.main()
