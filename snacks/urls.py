
from django.urls import path, include
from .views import SnackDeleteView, SnackCreateView, SnackUpdateView, SnackListView, SnackDetailView, 

urlpaterns = [
    path('', SnackListView.as_view(), name='snack_list'),  # Home Route
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'), # Detail is a single Item from the Model table
    # thus the path must indicate the value of the primary key
    path('new/', SnackCreateView.as_view(), name='snack_create'), # pathname indicates the purpose of the current View.
    path('<int:pk>/edit', SnackUpdateView.as_view(), name='snack_update'),
    path('<int:pk>/delete', SnackDeleteView.as_view(), name='snack_delete'),
]