from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Category, Comment


class TestViews(TestCase, Client):

    def setUp(self):
        """Set up before each text"""
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category')
        self.client = Client()
        self.browse_url = reverse('browse')
        
        post = Post.objects.create(
            title='Test title',
            slug='test-title',
            author=self.user,
            location='Test location',
            opening_time=1,
            closing_time=1,
            website='www.testurl.com',
            content='test content for test blog post',
            featured_image='test_img.jpeg',
            status=1,
            category=self.category
        )

    # def test_model_Post(self):
    #     
        
    #     self.assertEquals(str(post), 'Test title')
    #     self.assertTrue(isinstance(post, Post))

    def test_home_GET(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_browse_GET(self):
        response = self.client.get(self.browse_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'browse.html', 'base.html')

    # def test_browse_GET_not_logged_in(self):
    #     self.client.logout()
    #     response = self.client.get(self.browse_url)
    #     self.assertEquals(response.status_code, 302)
