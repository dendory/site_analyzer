import unittest
from app import app

class TestApp(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()

	def test_homepage(self):
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Site Analyzer', response.data)

	def test_submit_form(self):
		response = self.app.post('/', data=dict(input='https://google.com'))
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Success!', response.data)

if __name__ == '__main__':
	unittest.main()
