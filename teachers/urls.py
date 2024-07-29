from django.urls import path

from courses.views import IndexPage
from teachers.views import TeachersPage

urlpatterns = [
    path('', TeachersPage.as_view(), name='index'),
]
