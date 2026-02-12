import sys
import unittest

sys.path.insert(1, 'src')

import scanner

class TestScanGivenPort(unittest.TestCase):

    def test_open_port(self):
        self.assertEqual(scanner.scan_given_port('', 53), True)

    def test_closed_port(self):
        self.assertEqual(scanner.scan_given_port('', 9999), False)

if __name__ == '__main__':
    unittest.main()
