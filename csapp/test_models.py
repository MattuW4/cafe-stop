from django.test import TestCase
from .models import Post, Comment

class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        self.assertTrue(self.post.opening_time == 0)
        self.assertTrue(self.post.closing_time == 0)
        self.assertTrue(self.post.featured_image == 'placeholder')
        self.assertTrue(self.post.status == 1)
        self.assertTrue(self.comment.approved)
