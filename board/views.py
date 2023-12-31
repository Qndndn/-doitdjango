from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Board

# Create your views here.
class BoardList(ListView):
    model = Board
    ordering = '-pk'


class BoardDetail(DetailView):
    model = Board
    
class BoardCreate(LoginRequiredMixin, CreateView):
    model = Board
    fields = ['title', 'content']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            response = super(BoardCreate, self).for_valid(form)

            return response
        else:
            return redirect('/board/')