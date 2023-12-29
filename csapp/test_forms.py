from django.test import TestCase
from .forms import AddPostForm, UpdatePostForm, CommentForm

class TestAddPostForm(TestCase):

    def test_post_title_is_required(self):
        form = AddPostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_location_is_required(self):
        form = AddPostForm({'location': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('location', form.errors.keys())
        self.assertEqual(form.errors['location'][0], 'This field is required.')

    def test_post_opening_time_is_required(self):
        form = AddPostForm({'opening_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('opening_time', form.errors.keys())
        self.assertEqual(form.errors['opening_time'][0], 'This field is required.')

    def test_post_closing_time_is_required(self):
        form = AddPostForm({'closing_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('closing_time', form.errors.keys())
        self.assertEqual(form.errors['closing_time'][0], 'This field is required.')

    def test_post_category_is_required(self):
        form = AddPostForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    def test_post_content_is_required(self):
        form = AddPostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = AddPostForm()
        self.assertEqual(form.Meta.fields, ['title', 'location', 'opening_time', 'closing_time',
                  'website', 'category', 'content', 'featured_image'])

class TestUpdatePostForm(TestCase):

    def test_post_title_is_required(self):
        form = UpdatePostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_location_is_required(self):
        form = UpdatePostForm({'location': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('location', form.errors.keys())
        self.assertEqual(form.errors['location'][0], 'This field is required.')

    def test_post_opening_time_is_required(self):
        form = UpdatePostForm({'opening_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('opening_time', form.errors.keys())
        self.assertEqual(form.errors['opening_time'][0], 'This field is required.')

    def test_post_closing_time_is_required(self):
        form = UpdatePostForm({'closing_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('closing_time', form.errors.keys())
        self.assertEqual(form.errors['closing_time'][0], 'This field is required.')

    def test_post_content_is_required(self):
        form = UpdatePostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UpdatePostForm()
        self.assertEqual(form.Meta.fields, ['title', 'location', 'opening_time', 'closing_time',
                  'website', 'content', 'featured_image'])

class TestCommentForm(TestCase):

    def test_post_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))