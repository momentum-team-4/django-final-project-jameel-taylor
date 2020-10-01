from django.forms import Form, ModelForm, CharField, ModelChoiceField, ModelMultipleChoiceField, Textarea
from flashcards.models import Deck, Flashcard

class DeckCreateForm(ModelForm):
    class Meta:
        model = Deck
        fields = ['name']

class FlashcardCreateForm(ModelForm):
    class Meta:
        model = Flashcard
        fields = ['text_prompt', 'answer'] 

class AddFlashcardForm(Form):
    flashcard = ModelChoiceField(Flashcard.objects.all())