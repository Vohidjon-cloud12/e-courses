from django.urls import path

from blogs.views import BlogPage
from courses.views import IndexPage

urlpatterns = [
    path('', BlogPage.as_view(), name='index'),
]
