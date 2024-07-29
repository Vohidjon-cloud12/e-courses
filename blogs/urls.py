from django.urls import path

from blogs.views import BlogListPage, BlogDetailPage

urlpatterns = [
    path('blog/', BlogListPage.as_view(), name='blog'),
path('single/', BlogDetailPage.as_view(), name='single'),
]
