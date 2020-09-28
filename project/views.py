from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcards
# from .forms import FrontCard, BackCard

def deck_list(request):
    decks = Flashcards.objects.all()
    return render(request, "project/deck_list.html", {"flashcards": decks})

def deck_detail(request):
    deck = get_object_or_404(Flashcards, pk=pk)
    return render(request, "project/deck_detail.html", {"deck": deck})