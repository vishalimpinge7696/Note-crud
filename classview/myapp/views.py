from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Note
from . forms import NoteForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,   UpdateView, DeleteView


class NoteList(ListView):
    model = Note


class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm
    success_url = '../'


class NoteDetail(DetailView):
    model =  Note


class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    success_url = '../../'


class NoteDelete(DeleteView):
    model = Note
    success_url = '../../'
