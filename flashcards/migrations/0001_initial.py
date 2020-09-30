# Generated by Django 3.1.1 on 2020-09-29 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_prompt', models.TextField()),
                ('answer', models.TextField()),
                ('decks', models.ManyToManyField(related_name='flashcards', to='flashcards.Deck')),
            ],
        ),
    ]