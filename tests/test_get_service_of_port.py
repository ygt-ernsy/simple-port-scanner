import sys
import unittest

sys.path.insert(1, 'src')

import scanner

class TestGetServiceOfPort(unittest.TestCase):
    def test_known_port(self):
        self.assertEqual(scanner.get_service_of_port(53), 'domain')
    
    def test_unknown_port(self):
        self.assertEqual(scanner.get_service_of_port(38920), '')

if __name__ == '__main__':
    unittest.main()
