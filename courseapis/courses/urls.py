from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cate',views.CategoryViewSet,basename='category')
router.register('courses',views.CourseViewSet,basename="course")

urlpatterns = [
    path('', include(router.urls)),

]
