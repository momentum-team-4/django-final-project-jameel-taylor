from django.db import models

class Flashcard(models.Model):
    front = models.CharField(max_length=255, null=False, blank=False)
    back = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.front}"