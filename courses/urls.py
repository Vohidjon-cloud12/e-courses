from django.urls import path

from courses.views import CoursePage

urlpatterns = [
    path('course/', CoursePage.as_view(), name='course'),
]
