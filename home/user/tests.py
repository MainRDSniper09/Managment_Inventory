''' 
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm

class UserViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('user-register')
        self.login_url = reverse('user-login')
        self.profile_url = reverse('user-profile')
        self.profile_update_url = reverse('user-profile-update')
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    
    def test_register_view_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/register.html')
    
    def test_register_view_POST_valid(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras registro exitoso
        self.assertTrue(User.objects.filter(username='newuser').exists())
    
    def test_profile_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile.html')
    
    def test_profile_update_view_POST(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.profile_update_url, {
            'username': 'updateduser'
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras actualizar
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
'''