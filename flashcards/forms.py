from django.forms import Form, ModelForm, CharField, ModelMultipleChoiceField, Textarea
from flashcards.models import Deck, Flashcard

class DeckCreateForm(ModelForm):
    class Meta:
        model = Deck
        fields = ['name']

class FlashcardCreateForm(ModelForm):
    class Meta:
        model = Flashcard
        fields = ['text_prompt', 'answer'] 
