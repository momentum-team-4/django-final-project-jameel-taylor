from django.forms import Form, ModelForm, CharField, ModelMultipleChoiceField, Textarea
from flashcards.models import Deck

class DeckCreateForm(ModelForm):
    name = CharField(label='Deck Name', max_length=255)

class FlashcardCreateForm(ModelForm):
    text_prompt = CharField(label='Put question or prompt here', widget=Textarea)
    answer = CharField(label="Answer", widget=Textarea)
    decks = ModelMultipleChoiceField(queryset= Deck.objects.all())
