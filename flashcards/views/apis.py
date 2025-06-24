from rest_framework import viewsets, permissions, filters
from flashcards.models import Deck, Flashcard
from flashcards.serializers import DeckSerializer, FlashcardSerializer

class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.none()
    serializer_class = DeckSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'id']
    ordering = ['name']

    def get_queryset(self):
        return Deck.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.none()
    serializer_class = FlashcardSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['question', 'answer']

    def get_queryset(self):
        deck_id = self.request.query_params.get('deck')
        query = Flashcard.objects.filter(deck__user=self.request.user)
        if deck_id is None:
            return []
        
        return query.filter(deck_id=deck_id)
