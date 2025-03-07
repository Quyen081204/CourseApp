from rest_framework.generics import ListCreateAPIView

from  .models  import Category, Course, Lesson
from .serializers import CategorySerializer, CourseSerializer
from rest_framework import viewsets,generics
from .paginators import CoursePagination

class CategoryViewSet(viewsets.ViewSet,ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class =  CourseSerializer
    pagination_class =  CoursePagination

    def get_queryset(self):
        queryset = self.queryset

        q = self.request.query_params.get('q')
        if q:
            query = Course.objects.filter(subject__icontains=q)

        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            query = Course.objects.filter(category_id=cate_id)

        return queryset

