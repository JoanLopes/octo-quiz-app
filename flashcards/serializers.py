from rest_framework import serializers
from flashcards.models import Deck, Flashcard

class FlashcardSerializer(serializers.ModelSerializer):
    deck_name = serializers.CharField(source='deck.name', read_only=True)

    class Meta:
        model = Flashcard
        fields = ['id', 'question', 'answer', 'deck', 'deck_name', 'photo']

class DeckSerializer(serializers.ModelSerializer):
    flashcards = FlashcardSerializer(many=True, read_only=True)

    class Meta:
        model = Deck
        fields = ['id', 'name', 'description', 'flashcards']
