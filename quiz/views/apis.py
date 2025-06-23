from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from ..models import Category, Quiz, Question, Choice, Result, UserAnswer
from ..serializers import (
    CategorySerializer,
    QuizSerializer,
    QuestionSerializer,
    ChoiceSerializer,
    ResultSerializer,
    UserAnswerSerializer,
    SubmitQuizSerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category')
        if category_id:
            return self.queryset.filter(category_id=category_id)
        return self.queryset

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        quiz = self.get_object()
        questions = quiz.questions.prefetch_related('choices')
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class SubmitQuizView(generics.CreateAPIView):
    """
    Recebe as respostas do usuário e calcula a pontuação.
    """
    serializer_class = SubmitQuizSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(ResultSerializer(result).data, status=status.HTTP_201_CREATED)
