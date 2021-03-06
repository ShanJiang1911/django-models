from django.urls import path
from .views import SnackListView, SnackDetailView, AboutPageView

urlpatterns = [
    path("", SnackListView.as_view(), name="snacks_list"),
    path("<int:pk>/", SnackDetailView.as_view(), name="snack_detail"),
    path("about/", AboutPageView.as_view(), name="about"),
]