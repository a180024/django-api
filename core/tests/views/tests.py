from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from core.models import File
User = get_user_model()

class WithoutJWTTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
    def test_without_jwt(self):
        response = self.client.get(reverse('files:file-list'))
        self.assertEqual(response.status_code, 401)

class WithJWTTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        response = self.client.post('/auth/jwt/create', data={'username':'testuser', 'password':'pass'})    
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='JWT '+self.token)
        #  self.assertIsNotNone(token)
    def test_file_list_view(self):
        response = self.client.get(reverse('files:file-list'))
        self.assertEqual(response.status_code, 200)

    #  def test_upload_file(self):
        #  with open('/Users/davin/Desktop/example.txt') as fp:
            #  response = self.client.post(reverse('files:file-upload'), {'name': 'file', 'attachment': fp}, format='multipart')
        #  self.assertEqual(response.status_code, 201)




