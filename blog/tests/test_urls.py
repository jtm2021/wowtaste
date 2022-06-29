from django.test import SimpleTestCase
from blog.views import PostList
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):

    def test_post_list_url(self):
        url = reverse("home")
        self.assertEquals("/", url)
        self.assertEquals(resolve(url), PostList)