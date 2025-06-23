from django.contrib import admin
from flashcards.models import Deck, Flashcard

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'description')
    list_filter = ('user',)
    search_fields = ('name', 'description', 'user__username')
    ordering = ('id',)

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'deck', 'get_user')
    list_filter = ('deck__user',)
    search_fields = ('question', 'answer', 'deck__name', 'deck__user__username')
    ordering = ('id',)

    def get_user(self, obj):
        return obj.deck.user
    get_user.short_description = 'User'
