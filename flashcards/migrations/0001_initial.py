# Generated by Django 5.0.4 on 2025-06-23 06:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Deck',
                'verbose_name_plural': 'Decks',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flashcards', to='flashcards.deck')),
            ],
            options={
                'verbose_name': 'Flashcard',
                'verbose_name_plural': 'Flashcards',
                'db_table': '',
                'managed': True,
                'unique_together': {('deck', 'question')},
            },
        ),
    ]
