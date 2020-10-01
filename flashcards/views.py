from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from .models import Deck, Flashcard
from users.models import User
from .forms import DeckCreateForm, FlashcardCreateForm

import json


@login_required
def deck_list(request):
    deck = Deck.objects.all()
    context = {'decks': deck}
    return render(request, "decks/deck_list.html", context)

@login_required
def create_deck(request):
    if request.method == "GET":
        form = DeckCreateForm()
    else:
        form = DeckCreateForm(request.POST)
        
        if form.is_valid():
            # name = form.cleaned_data['name']
            # new_deck = Deck(name=name)
            # new_deck.save()
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect(to='deck_list')
    return render(request, 'decks/create_deck.html', {'form': form})

@login_required
def decks_update(request, pk):
    deck = get_object_or_404(Deck, pk=pk)

    if request.method == "GET":
        form = DeckCreateForm(instance=deck)
    else:
        form = DeckCreateForm(data=request.POST, instance=deck)
        if form.is_valid():
            form.save()
            success(request, "deck updated.")
            return redirect(to='deck_list')
    return render(request, "decks/deck_update.html", {"form": form})

@login_required
def deck_detail(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    return render(request, 'decks/deck_detail.html', {"deck": deck})

@login_required
def create_flashcards(request):
    if request.method == "GET":
        form = FlashcardCreateForm()
    else:
        form = FlashcardCreateForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.user = request.user
            flashcard.save()
            return redirect(to='deck_detail')
    return render(request, 'decks/create_flashcards.html', {'form': form})

@login_required
def delete_deck(request, pk):
    if request.method == "GET":
        return render(request, "decks/delete_deck.html")

    else:
        deck = get_object_or_404(Deck, pk=pk)
        deck.delete()
        success(request, "deck deleted.")

        return redirect(to="deck_list")

@login_required
def delete_flashcard(request, pk):
    if request.method == "GET":
        return render(request, "decks/flashcard_edit.html")
    else:
        deck = get_object_or_404(Deck, pk=pk)
        deck.delete()
        success(request, "flashcard deleted.")
        return redirect(to="deck_list")

def take_quiz(request, pk):
    if request.method == 'GET':
        return render(request, 'decks/quiz.html')