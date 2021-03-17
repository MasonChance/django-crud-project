
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Snack
from django.urls import reverse_lazy

#C--> CreateView
#R--> ListView, DetailView
#U--> UpdateView
#D--> DeleteView
# Create your views here.  

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    # because this view deals with forms it requires list of field names
    # for reference. fields are based on properties of the Model
    # the form is based on. 
    success_url = reverse_lazy('snack_list')
    fields = ['title', 'description', 'purchaser']

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['title', 'description', 'purchaser']

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')
    # reverse_lazy allows re-direct to the indicated view by view-name


