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
        
        """Post demo model"""
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
        """Comment demo model"""
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='test comment'
        )
        
    def test_post_model_str(self):
        """Test the __str__ method for post"""
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_comment_model_str(self):
        """Test the __str__ method for comment"""
        self.assertEqual(
            self.comment.__str__(),
            f'Comment {self.comment.body} by {self.comment.author}'
            )

    
    def test_post_defaults(self):
        """Test default values"""
        self.assertTrue(self.post.opening_time == 0)
        self.assertTrue(self.post.closing_time == 0)
        self.assertTrue(self.post.status == 0)
        self.assertTrue(self.comment.approved == False)