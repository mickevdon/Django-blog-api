from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title="A title",
            body="Body content",
        )

    def test_post_model(self):
        self.assertEqual(self.author.username, "testuser")
        self.assertEqual(self.post.title, "A title")
        self.assertEqual(self.post.body, "Body content")
        self.assertEqual(str(self.post, "A title"))
