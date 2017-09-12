import app
import unittest
import json

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_root(self):
        response = self.app.get('/')
        self.assertEqual(json.loads(response.data), dict(message='Hello World'))

    def test_metadata(self):
        response = self.app.get('/metadata')
        self.assertEqual(json.loads(response.data).keys(), ['lastcommitsha', 'version'])

    def test_health(self):
        response = self.app.get('/health')
        self.assertEqual(json.loads(response.data).keys(), ['status_code', 'response_time'])

if __name__ == '__main__':
    unittest.main()

