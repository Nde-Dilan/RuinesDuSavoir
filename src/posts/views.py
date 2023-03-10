from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from posts.models import *


# Create your views here.

class BlogpostHome(ListView):
    # queryset = Blogpost.objects.filter(published=True)
    model = Blogpost
    context_object_name = "posts"
    template_name = "posts/index.html"


class BlogpostCreate(CreateView):
    model = Blogpost
    template_name = "posts/create.html"
    fields = ["title", "content", ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Créer"
        return context


class BlogpostUpdate(UpdateView):
    model = Blogpost
    template_name = "posts/create.html"
    fields = ["title", "content", "published", ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Editer"
        return context


class BlogpostDelete(DeleteView):
    model = Blogpost
    template_name = "posts/delete.html"
    fields = ["title", "content", ]
    success_url = reverse_lazy("posts:home")
    context_object_name = "post"



class BlogpostDetail(DetailView):
    model = Blogpost
    template_name = "posts/detail.html"
    fields = ["title", "content", ]
    context_object_name = "post"
