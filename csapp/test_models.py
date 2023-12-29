from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Category, Comment

class TestModels(TestCase, Client):

    def setUp(self):
        """Set up before each test"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')        
        self.client.login(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category')
        self.user.save()
        
        self.post = Post.objects.create(
            title='Test title',
            slug='test-title',
            author=self.user,
            location='Test location',
            opening_time=0,
            closing_time=0,
            website='www.testurl.com',
            content='test content for test blog post',
            featured_image='test_img.jpeg',
            status=0,
            category=self.category
        )
        
        # self.assertEquals(str(post), 'Test title')
        # self.assertTrue(isinstance(post, Post))
    
    def test_post_defaults(self):
        """Test default values"""
        self.assertTrue(self.post.opening_time == 0)
        self.assertTrue(self.post.closing_time == 0)
        self.assertTrue(self.post.status == 0)
        # self.assertTrue(self.comment.approved)