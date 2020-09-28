from django.forms import Form, ModelForm, CharField, ChoiceField
from .models import Flashcards

class DeckForm(ModelForm):
    class Meta:
        model = Flashcards
        fields = [
            'front',
            'back',
        ]