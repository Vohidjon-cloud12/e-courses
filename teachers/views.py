from django.shortcuts import render
from django.views import View


class TeachersPage(View):
    def get(self, request):
        return render(request, 'teacher.html')

