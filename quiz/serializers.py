from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Category, Quiz, Question, Choice, Result, UserAnswer
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']


class QuizSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'category', 'time_limit', 'created_at']


class ResultSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Result
        fields = ['id', 'quiz', 'score', 'submitted_at']


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['question', 'selected_choice']


class SubmitQuizSerializer(serializers.Serializer):
    quiz_id = serializers.IntegerField()
    answers = UserAnswerSerializer(many=True)

    def validate(self, data):
        try:
            quiz = Quiz.objects.get(pk=data['quiz_id'])
        except Quiz.DoesNotExist:
            raise serializers.ValidationError("Quiz not found.")
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        quiz_id = validated_data['quiz_id']
        answers_data = validated_data['answers']

        quiz = Quiz.objects.get(pk=quiz_id)
        result = Result.objects.create(user=user, quiz=quiz, score=0)

        score = 0

        for answer_data in answers_data:
            question = answer_data['question']
            selected_choice = answer_data['selected_choice']

            UserAnswer.objects.create(
                result=result,
                question=question,
                selected_choice=selected_choice
            )

            if selected_choice.is_correct:
                score += 1

        result.score = score
        result.save()

        return result
