from django.test import TestCase
from blogapp.models import Blog
from django.urls import reverse
# Create your tests here.

class PostModelTests(TestCase):

    def setUp(self):
        pass

    def test_ListView(self):
        Blog.objects.create(title="title1",text="text1")
        Blog.objects.create(title="title2",text="text2")
        response = self.client.get(reverse('blog:list'))
        object_list = response.context['object_list']
        self.assertEqual(object_list.count(), 2)

    def test_DetailView(self):
        response = self.client.get(reverse('blog:detail',kwargs={'pk':1}))
        self.assertEqual(response.status_code, 404)

    def test_UpdateView(self):
        blog = Blog.objects.create(title="title1",text="text1")
        response = self.client.post(reverse('blog:update', kwargs={'pk': blog.id}), {'title': 'title123', 'text': 'text123'})
        blog2 = Blog.objects.get(id=blog.id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(blog2.title, "title123")
        self.assertEqual(blog2.text, "text123")
    
    def test_DeleteView(self):
        blog = Blog.objects.create(title="title1",text="text1")
        blog_all = Blog.objects.all()

        self.assertEqual(blog_all.count(), 1)

        response = self.client.delete(reverse('blog:delete', kwargs={'pk': blog.id}))
        self.assertEqual(response.status_code, 302)

        blog_all = Blog.objects.all()
        self.assertEqual(blog_all.count(), 0)
    

