from django.urls import path, include
from rest_framework.routers import DefaultRouter
from flashcards.views import DeckViewSet, FlashcardViewSet

router = DefaultRouter()
router.register(r'decks', DeckViewSet, basename='deck')
router.register(r'flashcards', FlashcardViewSet, basename='flashcard')

urlpatterns = [
    path('', include(router.urls)),
]
