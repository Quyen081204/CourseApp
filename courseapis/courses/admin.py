from django.contrib import admin
from courses.models import Category, Course,Lesson
from django.utils.html import mark_safe
# Register your models here.

class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject','active','created_date']
    search_fields  = ['subject']
    list_filter = ['id', 'created_date']
    readonly_fields = ['image_view']

    def image_view(self,course):
        return mark_safe(f"<img src='/static/{course.image.name}' width='80'/>")


admin.site.register(Category)
admin.site.register(Course,MyCourseAdmin)
admin.site.register(Lesson)