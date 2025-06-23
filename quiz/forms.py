from django import forms
from quiz.models import Category, Quiz, Question, Choice

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'category', 'time_limit']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quiz', 'text']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question', 'text', 'is_correct']
