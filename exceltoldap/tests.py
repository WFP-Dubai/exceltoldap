from django.test import TestCase


class ExcelViewTestCase(TestCase):
    def test_users(self):
        resp = self.client.get('/users/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('users' in resp.context)
    def test_vheicles(self):
        resp = self.client.get('/vehicles/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('vehicles' in resp.context)
        
        