# Generated by Django 3.1.1 on 2020-10-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0003_remove_flashcard_decks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='flashcards',
        ),
        migrations.AddField(
            model_name='flashcard',
            name='decks',
            field=models.ManyToManyField(to='flashcards.Deck'),
        ),
    ]
