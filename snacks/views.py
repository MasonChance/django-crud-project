from models import Snack
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView,
from .models import Snack
from django.urls import reverse_lazy

#C--> CreateView
#R--> ListView, DetailView
#U--> UpdateView
#D--> DeleteView
# Create your views here.

class SnackListView(ListView):
    template_name = 'snack_list'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snack_create'
    model = Snack
    fields = ['title', 'description', 'purchaser']

class SnackUpdateView(UpdateView):
    template_name = 'snack_update'
    model = Snack
    fields = ['title', 'description', 'purchaser']

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete'
    model = Snack
    success_url = reverse_lazy('snack_list')


