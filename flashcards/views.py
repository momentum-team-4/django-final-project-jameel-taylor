from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from .models import Deck, Flashcard
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
            name = form.cleaned_data['name']
            new_deck = Deck(name=name)
            new_deck.save()
            return HttpResponseRedirect('/decks/')
    return redirect(request, 'create_deck.html', {'form': DeckCreateForm()})

@login_required
def create_flashcards(request):
    if request.method == "GET":
        form = FlashcardCreateForm(request.POST)
        if form.is_valid():
            text_prompt = form.cleaned_data['text_prompt']
            answer = form.cleaned_data['answer']
            decks = form.cleaned_data['decks']
# https://docs.djangoproject.com/en/3.1/topics/forms/

            if text_prompt and answer and decks:
                new_flashcard = Flashcard(text_prompt=text_prompt, answer=answer)
                new_flashcard.save()
                new_flashcard.decks.add(*decks)
                new_flashcard.save()
                return HttpResponseRedirect('/decks/')
        return render(request, 'flashcard_create.html', {'form': FlashcardCreateForm()})



@login_required
def delete_deck(request, pk):
    if request.method == "GET":
        return render(request, "deck/delete_deck.html")

    else:
        deck = get_object_or_404(Deck, pk=pk)
        deck.delete()
        success(request, "deck deleted.")

        return redirect(to="deck_list")