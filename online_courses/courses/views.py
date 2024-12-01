from django.shortcuts import render
from django.urls import path, include
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Course, Lesson, Comment,Student
from .serializers import CourseSerializer, LessonSerializer, CommentSerializer,StudentSerializer

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
#from .views import CourseViewSet, LessonViewSet, CommentViewSet,StudentViewSet


# Kurslar API
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

# Darslar API
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

# Izohlar API
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]





from django_filters import rest_framework as filters
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer


class CourseFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    active = filters.BooleanFilter()

    class Meta:
        model = Course
        fields = ['title', 'active']


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_class = CourseFilter
    permission_classes = [IsAuthenticated]



# Create your views here.


# class StudentApiView(generic.ListCreateApiView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
#
#
#
# class StudentDetailApiView(generic.RetrieveUpdateStudenteDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer