from django.urls import path
from teachers.views import TeachersPage

urlpatterns = [
    path('teacher/', TeachersPage.as_view(), name='teacher'),
]
