from django.contrib import admin

from courses.models import Course, Category, CourseVideo, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(CourseVideo)
admin.site.register(Comment)

