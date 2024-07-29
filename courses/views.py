from django.shortcuts import render
from django.views import View


class CoursePage(View):
    def get(self, request):
        return render(request, 'course.html')
