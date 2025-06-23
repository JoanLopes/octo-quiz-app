from django.urls import path
from quiz.views import (
    # Categories
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    # Quizzes
    QuizListView, QuizCreateView, QuizUpdateView, QuizDeleteView,
    # Questions
    QuestionListView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView,
    # Choices
    ChoiceListView, ChoiceCreateView, ChoiceUpdateView, ChoiceDeleteView,
    # Results
    ResultListView,
    # User Answers
    UserAnswerListView,
)

urlpatterns = [
    # Categories
    path('categories/', CategoryListView.as_view(), name='category-list-page'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create-page'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-update-page'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete-page'),

    # Quizzes
    path('quizzes/', QuizListView.as_view(), name='quiz-list-page'),
    path('quizzes/create/', QuizCreateView.as_view(), name='quiz-create-page'),
    path('quizzes/<int:pk>/edit/', QuizUpdateView.as_view(), name='quiz-update-page'),
    path('quizzes/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz-delete-page'),

    # Questions
    path('questions/', QuestionListView.as_view(), name='question-list-page'),
    path('questions/create/', QuestionCreateView.as_view(), name='question-create-page'),
    path('questions/<int:pk>/edit/', QuestionUpdateView.as_view(), name='question-update-page'),
    path('questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete-page'),

    # Choices
    path('choices/', ChoiceListView.as_view(), name='choice-list-page'),
    path('choices/create/', ChoiceCreateView.as_view(), name='choice-create-page'),
    path('choices/<int:pk>/edit/', ChoiceUpdateView.as_view(), name='choice-update-page'),
    path('choices/<int:pk>/delete/', ChoiceDeleteView.as_view(), name='choice-delete-page'),

    # Results
    path('results/', ResultListView.as_view(), name='result-list-page'),

    # User Answers
    path('answers/', UserAnswerListView.as_view(), name='useranswer-list-page'),
]
