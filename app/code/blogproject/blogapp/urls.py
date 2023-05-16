from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='top'),
    path('post', views.BlogPostView.as_view(), name='post'),
    path('delete/<int:pk>', views.BlogDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.BlogUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', views.BlogDetailView.as_view(), name='detail'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

]