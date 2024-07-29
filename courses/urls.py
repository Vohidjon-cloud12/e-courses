from django.urls import path

from courses.views import IndexPage

urlpatterns = [
    path('index/', IndexPage.as_view(), name='index'),
]
