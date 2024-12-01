from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, CommentViewSet
#from .views import StudentApiView, CourseAPIView, StudentDetailApiView

# router = DefaultRouter()
# router.register(r'courses', CourseViewSet)
# router.register(r'lessons', LessonViewSet)
# router.register(r'comments', CommentViewSet)

urlpatterns = [
#    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#    path('students/', StudentApiView.as_view()),
#    path('students/<int:student_id>/', StudentDetailApiView.as_view(), name='student-detail'),
#    path('courses/', CourseAPIView.as_view()),
#    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course-detail'),
]

