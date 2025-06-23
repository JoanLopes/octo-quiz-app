from django.contrib import admin
from .models import Category, Quiz, Question, Choice, Result, UserAnswer


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'time_limit', 'created_at']
    list_filter = ['category']
    search_fields = ['title', 'description']
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'quiz']
    search_fields = ['text']
    list_filter = ['quiz']
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'question', 'is_correct']
    list_filter = ['is_correct']
    search_fields = ['text']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'quiz', 'score', 'submitted_at']
    list_filter = ['quiz', 'submitted_at']
    search_fields = ['user__username', 'quiz__title']


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'result', 'question', 'selected_choice']
    search_fields = ['result__user__username', 'question__text']
