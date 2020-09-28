from django.db import models

class Flashcards(models.Model):
    front = models.CharField(max_length=255, null=False, blank=False)
    back = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.front}"
# shows full card, question and answer in deck


class FrontCard(models.Model):
    pass
# show only front of card when studying

class BackCard(models.Model):
    pass
# show only back when answer is correc or incorrect