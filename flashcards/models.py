from django.contrib.auth.models import User
from django.db import models

class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='decks')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Deck'
        verbose_name_plural = 'Decks'

class Flashcard(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='flashcards')
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Flashcard'
        verbose_name_plural = 'Flashcards'
        unique_together = (('deck', 'question'),)
