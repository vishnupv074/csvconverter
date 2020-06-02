from django.urls import path
from . import views

urlpatterns = [
    path('', views.csv_view, name="json_to_csv"),
    path('<str:id>', views.csv_view, name="to_csv_have_id"),
]
