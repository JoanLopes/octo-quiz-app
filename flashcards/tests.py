from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Deck, Flashcard
from rest_framework_simplejwt.tokens import RefreshToken

class BaseTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='123456')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

class DeckTests(BaseTest):
    def test_create_deck(self):
        data = {'name': 'Deck 1', 'description': 'Descrição do Deck 1'}
        response = self.client.post('/api/decks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Deck 1')

    def test_list_decks(self):
        Deck.objects.create(name='Deck Existente', user=self.user)
        response = self.client.get('/api/decks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_deck(self):
        deck = Deck.objects.create(name='Deck 2', user=self.user)
        data = {'name': 'Deck 2 Updated', 'description': 'Atualizado'}
        response = self.client.put(f'/api/decks/{deck.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Deck 2 Updated')

    def test_delete_deck(self):
        deck = Deck.objects.create(name='Deck 3', user=self.user)
        response = self.client.delete(f'/api/decks/{deck.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class FlashcardTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.deck = Deck.objects.create(name='Deck para Flashcards', user=self.user)

    def test_create_flashcard(self):
        data = {'deck': self.deck.id, 'question': 'Qual a cor do céu?', 'answer': 'Azul'}
        response = self.client.post('/api/flashcards/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['question'], 'Qual a cor do céu?')

    def test_list_flashcards(self):
        Flashcard.objects.create(deck=self.deck, question='Q1', answer='A1')
        response = self.client.get('/api/flashcards/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_flashcard(self):
        flashcard = Flashcard.objects.create(deck=self.deck, question='Q2', answer='A2')
        data = {'deck': self.deck.id, 'question': 'Q2 Atualizada', 'answer': 'A2 Atualizada'}
        response = self.client.put(f'/api/flashcards/{flashcard.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question'], 'Q2 Atualizada')

    def test_delete_flashcard(self):
        flashcard = Flashcard.objects.create(deck=self.deck, question='Q3', answer='A3')
        response = self.client.delete(f'/api/flashcards/{flashcard.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
