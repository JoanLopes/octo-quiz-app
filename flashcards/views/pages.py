from django.views.generic import TemplateView

class DeckListView(TemplateView):
    template_name = 'deck/deck_list.html'

class DeckCreateView(TemplateView):
    template_name = 'deck/deck_form.html'

class DeckUpdateView(TemplateView):
    template_name = 'deck/deck_form.html'

class DeckDeleteView(TemplateView):
    template_name = 'deck/deck_confirm_delete.html'

class FlashcardListView(TemplateView):
    template_name = 'flashcards/flashcard_list.html'

class FlashcardCreateView(TemplateView):
    template_name = 'flashcards/flashcard_form.html'

class FlashcardUpdateView(TemplateView):
    template_name = 'flashcards/flashcard_form.html'

class FlashcardDeleteView(TemplateView):
    template_name = 'flashcards/flashcard_confirm_delete.html'
