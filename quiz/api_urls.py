from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quiz.views import (
    CategoryViewSet,
    QuizViewSet,
    ResultViewSet,
    SubmitQuizView,
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'results', ResultViewSet, basename='result')

urlpatterns = [
    path('', include(router.urls)),
    path('submit-quiz/', SubmitQuizView.as_view(), name='submit-quiz'),
]
