from django.views.generic import ListView, DetailView   # new
from django.views.generic.edit import CreateView, UpdateView, DeleteView # new
from .models import Post
from django.urls import reverse_lazy    # new  to do delele

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'         # какой шаблон подгружать. базовый 

# класс для детализации поста
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# класс для создания поста
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

# класс для обновления поста
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'            # шаблон подгружать
    fields = ['title','author', 'body']         # какие поля выводить для обновления

# класс для удаления поста
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'      # шаблон какой подгружать
    success_url = reverse_lazy('home')      # возврат на старницу home