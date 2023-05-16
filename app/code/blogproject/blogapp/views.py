from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from .Form import BookForm
from django.views.generic import TemplateView,ListView,FormView,CreateView,DeleteView,DetailView,UpdateView
from django.contrib.auth.views import (LoginView,LogoutView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .Form import LoginForm
import datetime

class Login(LoginView):
    form_class = LoginForm
    template_name = "blogproject/login.html"


class Logout(LogoutView):
    template_name = "blogproject/login.html"


# Create your views here.
class BlogTopView(TemplateView):
    template_name = "blogproject/top.html"

class BlogListView(ListView):
    paginate_by = 5
    template_name = "blogproject/list.html"
    queryset = Book.objects.all()


    def trancerate_date(self,model):
        setattr(model, 'date', model.date.strftime('%Y年/%m月/%d日'))
        return model


    def get_context_data(self, *, object_list=None, **kwargs):


        """Get the context for this view."""
        queryset = object_list if object_list is not None else self.object_list
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        queryset = list(map(self.trancerate_date, queryset))

        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)

            if page.number -5 <=1:
                prev = [i for i in range(2,page.number)]
            else:
                prev = [i for i in range(page.number -5,page.number)]

            if page.number +5>=page.paginator.num_pages:
                nextpage = [i for i in range(page.number+1,page.paginator.num_pages)]
            else:
                nextpage = [i for i in range(page.number +1,page.number +6)]


            context = {
                'paginator': paginator,
                'prev':prev,
                'page_obj': page,
                'next':nextpage,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return context

class BlogPostView(CreateView):
    template_name = "blogproject/post.html"
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('blog:top')

class BlogDeleteView(DeleteView):
    template_name = "blogproject/delete.html"
    model = Book
    success_url = reverse_lazy('blog:top')

class BlogDetailView(DetailView):
    template_name = "blogproject/detail.html"
    model = Book

class BlogUpdateView(UpdateView):
    template_name = "blogproject/update.html"
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('blog:top')