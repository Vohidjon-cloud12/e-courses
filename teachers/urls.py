from django.urls import path
from teachers.views import TeachersPage

urlpatterns = [
    path('teachers/', TeachersPage.as_view(), name='teacher'),
]
