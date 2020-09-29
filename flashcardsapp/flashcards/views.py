from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import success, error
from .models import Flashcards
from .forms import DeckForm
from django.contrib.auth.forms import UserCreationForm


def create_account(request):
    form = Create_Account()
    return render(request,'register.html', {'form':form})

def deck_list(request):
    decks = Flashcards.objects.all()
    return render(request, "decks/deck_list.html", {"flashcards": decks})

def deck_detail(request):
    deck = get_object_or_404(Flashcards, pk=pk)
    return render(request, "decks/deck_detail.html", {"deck": deck})


def create_deck(request):
    if request.method == "GET":
        deck = DeckForm()
    else:
        deck = DeckForm(data=request.POST)

        if deck.is_valid():
            deck.save()

            success(request, "New deck created.")
            return redirect(to='deck_list')
    return render(request, "decks/create_deck.html", {"deck": deck})


