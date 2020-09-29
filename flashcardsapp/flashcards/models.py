from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

class Flashcard(models.Model):
    text_prompt = models.TextField()
    answer = models.TextField()
    decks = models.ManyToManyField(Deck, related_name="flashcards")