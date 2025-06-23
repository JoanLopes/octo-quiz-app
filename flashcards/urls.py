from django.urls import path
from . import views

urlpatterns = [
    path('decks/', views.DeckListView.as_view(), name='deck-list-page'),
    path('decks/create/', views.DeckCreateView.as_view(), name='deck-create-page'),
    path('decks/<int:pk>/edit/', views.DeckUpdateView.as_view(), name='deck-edit-page'),
    path('decks/<int:pk>/delete/', views.DeckDeleteView.as_view(), name='deck-delete-page'),

    path('flashcards/', views.FlashcardListView.as_view(), name='flashcard-list-page'),
    path('flashcards/create/', views.FlashcardCreateView.as_view(), name='flashcard-create-page'),
    path('flashcards/<int:pk>/edit/', views.FlashcardUpdateView.as_view(), name='flashcard-edit-page'),
    path('flashcards/<int:pk>/delete/', views.FlashcardDeleteView.as_view(), name='flashcard-delete-page'),
]