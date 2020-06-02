from django.urls import path
from . import views

urlpatterns = [
    path('', views.csv_view, name="json_to_csv"),  # For creating csv for given json
    path('<str:id>', views.csv_view, name="to_csv_have_id"),  # For creating a csv for file having different id
]
