"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView
from users import views as users_views
from flashcards import views as flashcards_views
from flashcards.models import Deck


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/flashcards/deck_list/')),
    path('login_required/', flashcards_views.login_required, name='login_required'),
    
    path('flashcards/deck_list/', flashcards_views.deck_list, name='deck_list'),
    path('flashcards/deck_detail/<int:pk>/', flashcards_views.deck_detail, name='deck_detail'),
    path('flashcards/create_deck/', flashcards_views.create_deck, name='create_deck'),
    path('flashcards/create_flashcards/', flashcards_views.create_flashcards, name='create_flashcards'),
    path('flashcards/update/<int:pk>/', flashcards_views.decks_update, name='decks_update'),
    path('flashcards/quiz/<int:pk>/', flashcards_views.take_quiz, name='take_quiz'),

    path('users/create/', users_views.users_create, name='users_create'),
    path('users/login/', users_views.users_login, name='users_login'),
    path('users/logout/', users_views.users_logout, name='users_logout')
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
