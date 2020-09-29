from django.forms import Form, ModelForm, CharField, ModelMultipleChoiceField, Textarea
from .models import Deck

class DeckCreateForm(Form):
    name = CharField(label='Deck Name', max_length=255)

class FlashcardCreateForm(Form):
    text_prompt = CharField(label='Put question or prompt here', widget=Textarea)
    answer = CharField(label="Answer", widget=Textarea)
    decks = ModelMultipleChoiceField(queryset= Deck.objects.all())