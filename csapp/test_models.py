from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Category, Comment

class TestModels(TestCase, Client):

    def setUp(self):
        """Set up before each text"""
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category')

    def test_model_Post(self):
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
        
        self.assertEquals(str(post), 'Test title')
        self.assertTrue(isinstance(post, Post))
    
    # def test_post_defaults(self):
    #     """Test default values"""
        # self.assertTrue(self.post.opening_time == 0)
        # self.assertTrue(self.post.closing_time == 0)
        # self.assertTrue(self.post.status == 0)
        # self.assertTrue(self.comment.approved)