from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from quiz.models import Category, Quiz, Question, Choice, Result, UserAnswer
from quiz.forms import CategoryForm, QuizForm, QuestionForm, ChoiceForm


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    extra_context = {
        'model_verbose_name': Category._meta.verbose_name.title(),
        'model_verbose_name_plural': Category._meta.verbose_name_plural.title(),
        'create_url_name': 'category-create-page',
        'update_url_name': 'category-update-page',
        'delete_url_name': 'category-delete-page',
    }

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'form.html'
    success_url = reverse_lazy('category-list')
    extra_context = {
        'model_verbose_name': Category._meta.verbose_name.title(),
    }

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'form.html'
    success_url = reverse_lazy('category-list')
    extra_context = {
        'model_verbose_name': Category._meta.verbose_name.title(),
    }

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('category-list')
    extra_context = {
        'model_verbose_name': Category._meta.verbose_name.title(),
    }


class QuizListView(LoginRequiredMixin, ListView):
    model = Quiz
    template_name = 'quiz_list.html'
    context_object_name = 'quizzes'
    extra_context = {
        'model_verbose_name': Quiz._meta.verbose_name.title(),
        'model_verbose_name_plural': Quiz._meta.verbose_name_plural.title(),
        'create_url_name': 'quiz-create-page',
        'update_url_name': 'quiz-update-page',
        'delete_url_name': 'quiz-delete-page',
    }

class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'form.html'
    success_url = reverse_lazy('quiz-list')
    extra_context = {
        'model_verbose_name': Quiz._meta.verbose_name.title(),
    }

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class QuizUpdateView(LoginRequiredMixin, UpdateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'form.html'
    success_url = reverse_lazy('quiz-list')
    extra_context = {
        'model_verbose_name': Quiz._meta.verbose_name.title(),
    }

class QuizDeleteView(LoginRequiredMixin, DeleteView):
    model = Quiz
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('quiz-list')
    extra_context = {
        'model_verbose_name': Quiz._meta.verbose_name.title(),
    }


class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'
    extra_context = {
        'model_verbose_name': Question._meta.verbose_name.title(),
        'model_verbose_name_plural': Question._meta.verbose_name_plural.title(),
        'create_url_name': 'question-create-page',
        'update_url_name': 'question-update-page',
        'delete_url_name': 'question-delete-page',
    }

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'form.html'
    success_url = reverse_lazy('question-list')
    extra_context = {
        'model_verbose_name': Question._meta.verbose_name.title(),
    }

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'form.html'
    success_url = reverse_lazy('question-list')
    extra_context = {
        'model_verbose_name': Question._meta.verbose_name.title(),
    }

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('question-list')
    extra_context = {
        'model_verbose_name': Question._meta.verbose_name.title(),
    }


class ChoiceListView(LoginRequiredMixin, ListView):
    model = Choice
    template_name = 'choice_list.html'
    context_object_name = 'choices'
    extra_context = {
        'model_verbose_name': Choice._meta.verbose_name.title(),
        'model_verbose_name_plural': Choice._meta.verbose_name_plural.title(),
        'create_url_name': 'choice-create-page',
        'update_url_name': 'choice-update-page',
        'delete_url_name': 'choice-delete-page',
    }

class ChoiceCreateView(LoginRequiredMixin, CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'form.html'
    success_url = reverse_lazy('choice-list')
    extra_context = {
        'model_verbose_name': Choice._meta.verbose_name.title(),
    }

class ChoiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'form.html'
    success_url = reverse_lazy('choice-list')
    extra_context = {
        'model_verbose_name': Choice._meta.verbose_name.title(),
    }

class ChoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Choice
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('choice-list')
    extra_context = {
        'model_verbose_name': Choice._meta.verbose_name.title(),
    }


class ResultListView(LoginRequiredMixin, ListView):
    model = Result
    template_name = 'result_list.html'
    context_object_name = 'results'
    extra_context = {
        'model_verbose_name': Result._meta.verbose_name.title(),
        'model_verbose_name_plural': Result._meta.verbose_name_plural.title(),
    }

    def get_queryset(self):
        return Result.objects.filter(user=self.request.user)


class UserAnswerListView(LoginRequiredMixin, ListView):
    model = UserAnswer
    template_name = 'useranswer_list.html'
    context_object_name = 'answers'
    extra_context = {
        'model_verbose_name': UserAnswer._meta.verbose_name.title(),
        'model_verbose_name_plural': UserAnswer._meta.verbose_name_plural.title(),
    }

    def get_queryset(self):
        return UserAnswer.objects.filter(result__user=self.request.user)
