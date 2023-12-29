from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Category, Comment


class TestViews(TestCase, Client):

    def setUp(self):
        """Set up before each test"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')        
        self.client.login(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category')
        
        """Post demo model"""
        self.post = Post.objects.create(
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

        """Comment demo model"""
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='test comment'
        )

        """Urls for test reverses"""
        self.browse_url = reverse('browse')
        self.add_post_url = reverse('add')
        self.update_post_url = reverse('update', args=[self.post.slug])
        self.delete_post_url = reverse('delete', args=[self.post.id])
        self.post_comment_url = reverse('post_detail', args=[self.post.slug])
        self.category_view_url = reverse('category_search', args=[self.category.name])
        
    def test_home_GET(self):
        """Test to check home page is accessible when not logged in"""
        self.client.logout()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_GET(self):
        """Test to check home page is accessible"""
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_browse_GET(self):
        """Test to check browse page is accessible"""
        response = self.client.get(self.browse_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'browse.html', 'base.html')

    def test_browse_GET_not_logged_in(self):
        """Test to check browse page is accessible when not logged in"""
        self.client.logout()
        response = self.client.get(self.browse_url)
        self.assertEquals(response.status_code, 200)

    def test_add_post_POST(self):
        """Test to check add post feature writes to database"""
        response = self.client.post(self.add_post_url, {
            'title': 'Test title 2',
            'slug': 'test-title-2',
            'author': self.user.id,
            'location': 'Test location 2',
            'opening_time': 2,
            'closing_time': 2,
            'website': 'www.testurl2.com',
            'content': 'test content for test blog post 2',
            'featured_image': 'test_img_2.jpeg',
            'status': 1,
            'category': self.category.id
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.count(), 2)
        self.assertEquals(Post.objects.last().title, 'Test title')

    def test_post_no_data_POST(self):
        """Test to check add post feature does not write to database with no data"""
        response = self.client.post(self.add_post_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Post.objects.count(), 1)

    def test_post_update_POST(self):
        """Test to check update post feature updates database"""
        response = self.client.post(self.update_post_url, {
            'title': 'Test title 3',
            'slug': 'test-title-2',
            'author': self.user.id,
            'location': 'Test location 3',
            'opening_time': 2,
            'closing_time': 2,
            'website': 'www.testurl3.com',
            'content': 'test content for test blog post 2',
            'featured_image': 'test_img_2.jpeg',
            'status': 1,
            'category': self.category.id
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.first().title, 'Test title 3')
        self.assertEquals(Post.objects.count(), 1)

    def test_delete_POST_DELETE(self):
        """Test to check delete post feature deletes data from database"""
        response = self.client.delete(self.delete_post_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Post.objects.count(), 0)

    def test_post_comment(self):
        """Test post commenting feature"""
        response = self.client.post(self.post_comment_url, {
            'body': 'test comment',
            })
        self.assertEquals(Comment.objects.last().body, 'test comment')

    def test_get_category_view(self):
        """ Test Category page retrieval and template usage """
        response = self.client.get(self.category_view_url)            
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories.html', 'base.html')
      



