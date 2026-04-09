import unittest
from flask import Flask
from src.routes.api import app as api_app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = api_app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_get_records(self):
        response = self.client.get('/api/records')
        self.assertEqual(response.status_code, 200)

    def test_create_record(self):
        response = self.client.post('/api/records', json={
            'name': 'Test Record',
            'category': 'Test Category',
            'status': 'active'
        })
        self.assertEqual(response.status_code, 201)

    def test_update_record(self):
        response = self.client.put('/api/records/1', json={
            'name': 'Updated Record',
            'category': 'Updated Category',
            'status': 'inactive'
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_record(self):
        response = self.client.delete('/api/records/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()