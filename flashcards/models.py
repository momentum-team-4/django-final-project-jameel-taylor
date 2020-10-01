from django.db import models
from users.models import User

class Deck(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
   

    def __str__(self):
        return f"{self.name}"

class Flashcard(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_prompt = models.TextField()
    answer = models.TextField()
    decks = models.ManyToManyField(Deck)

    # https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/