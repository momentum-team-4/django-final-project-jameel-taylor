from django.contrib import admin

# Register your models here.

from flashcards.models import Deck, Flashcard

admin.site.register(Deck)
admin.site.register(Flashcard)