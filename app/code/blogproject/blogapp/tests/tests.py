from django.test import TestCase
from blogapp.models import Blog
from django.urls import reverse
# Create your tests here.

class PostModelTests(TestCase):
    def test_is_empty(self):
        model_len = Blog.objects.all()
        self.assertEqual(model_len.count(), 0)
    
    def test_is_post(self):
        data = {"title":"test","text":"text"}
        Blog.objects.create(**data)
        # blog = Blog(**data)
        # blog.save()
        self.assertEqual(Blog.objects.all().count(), 1)

    def test_top(self):
        response = self.client.get(reverse("blog:top"))
        self.assertEqual(response.status_code, 200) 

    def test_list(self):
        Blog.objects.create(title="test1",text="test")
        Blog.objects.create(title="test2",text="test")

        response = self.client.get(reverse("blog:list"))
        # print(response.context["object_list"])
        self.assertQuerysetEqual(response.context["object_list"], ['<Blog: test1>', '<Blog: test2>'],ordered=False)
        # self.assertContains(response.context["object_list"], "test1")
        # self.assertContains(response.context["object_list"], "test2")

        # self.assertEqual(response.status_code, 200) 