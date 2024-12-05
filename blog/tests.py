from django.test import TestCase
from .models import BlogPost

class BlogPostTestCase(TestCase):
    def test_create_blog_post(self):
        post = BlogPost.objects.create(title="Test", content="Test content")
        self.assertEqual(post.title, "Test")
