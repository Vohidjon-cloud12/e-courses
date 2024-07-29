from django.shortcuts import render
from django.views import View


class CoursePage(View):
    def get(self, request):
        return render(request, 'course.html')

class AboutPage(View):
    def get(self, request):
        return render(request, 'about.html')

class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')


class ContactPage(View):
    def get(self, request):
        return render(request, 'contact.html')
