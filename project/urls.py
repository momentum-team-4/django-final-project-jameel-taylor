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
from django.views.generic import ListView, TemplateView
from users import views as users_views
from flashcards import views as flashcards_views
from flashcards.models import Deck


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="base.html")),
    path('login_required/', flashcards_views.login_required, name='login_required'),
    path('flashcards/create/', flashcards_views.create_deck, name='flashcards_create'),
    path('flashcards/create/', flashcards_views.create_flashcards, name='flashcards_create'),
    path('flashcards/update/<int:pk>/', flashcards_views.decks_update, name='deck_update'),

    # path('users/create/', users_views.users_create, name='users_create'),
    # path('users/login/', users_views.users_login, name='users_login'),
    # path('users/logout/', users_views.users_logout, name='users_logout')
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', TemplateView.as_view(template_name ='base.html')),
#     path('', views.deck_list, name="deck_list"),
#     path('register/', views.create_account, name='create_account'),
#     path('decks/', ListView.as_view(queryset=Deck.objects.all(),template_name='deck_list.html')),
#     path('decks/<int:deck_id>/',views.deck_list),
#     path('create/deck/', views.create_deck),
#     path('create/flashcard/', views.create_flashcards)
#     ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
