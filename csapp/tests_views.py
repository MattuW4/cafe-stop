from django.test import TestCase

class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_get_browse_post_page(self):
        response = self.client.get('browse')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'browse.html', 'base.html')

    def test_get_view_post_page(self):
        response = self.client.get('<slug:slug>/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html', 'base.html')

    def test_get_add_post_page(self):
        response = self.client.get('add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_add.html', 'base.html')

    def test_get_update_post_page(self):
        response = self.client.get('post/update/<slug:slug>')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_update.html', 'base.html')

    def test_get_delete_post_page(self): 
        response = self.client.get('post/<int:pk>/remove')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_delete.html', 'base.html')

    def test_get_category_search_page(self): 
        response = self.client.get('category/<category>/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories.html', 'base.html')

    def test_get_comment_like_views(self):
        response = self.client.get('like/<slug:slug>')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail, args=[slug]', 'base.html')



