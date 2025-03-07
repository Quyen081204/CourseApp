from rest_framework.pagination import PageNumberPagination

from .models import Category

class CoursePagination(PageNumberPagination):
    page_size = 1
