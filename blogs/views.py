from django.shortcuts import render
from django.views import View


class BlogListPage(View):
    def get(self, request):
        return render(request, 'blog.html')


class BlogDetailPage(View):
    def get(self, request):
        return render(request, 'single.html')