from django.urls import path

from courses.views import CoursePage, AboutPage, HomePage, ContactPage

urlpatterns = [
    path('course/', CoursePage.as_view(), name='course'),
    path('about/', AboutPage.as_view(), name='about'),
    path('home/', HomePage.as_view(), name='home'),
    path('contact/', ContactPage.as_view(), name='contact'),
]
