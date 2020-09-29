from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from .models import Deck, Flashcard
from users.model import User
from .forms import DeckCreateForm, FlashcardCreateForm

import json




@login_required
def deck_list(request, pk):
    deck = Deck.objects.get()
    context = {'deck': deck, 'flashcards': deck.flashcards.all()}
    return render(request, "templates/decks/deck_list.html", context)

@login_required
def create_deck(request):
    if request.method == "GET":
        form = DeckCreateForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # new_deck = Deck(name=name)
            # new_deck.save()
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return HttpResponseRedirect('/decks/')
    return redirect(request, 'create_deck.html', {'form': DeckCreateForm()})

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
def create_flashcards(request):
    if request.method == "GET":
        form = FlashcardCreateForm()
    else:
        form = FlashcardCreateForm(data=request.POST)        
        if form.is_valid():
# https://docs.djangoproject.com/en/3.1/topics/forms/
            form.save()
            return HttpResponseRedirect('/decks/')
    return render(request, 'flashcard_create.html', {'form': form})



@login_required
def delete_deck(request, pk):
    if request.method == "GET":
        return render(request, "deck/delete_deck.html")

    else:
        deck = get_object_or_404(Deck, pk=pk)
        deck.delete()
        success(request, "deck deleted.")

        return redirect(to="deck_list")