from django.urls import path
from . import views
from .views import UserRegistrationAPIView

urlpatterns = [
    # user
    path("register/", UserRegistrationAPIView.as_view(), name="user-registration"),
    # ingredients
    path("ingredients/", views.IngredientListView.as_view(), name="ingredient-list"),
    path(
        "ingredients/create/",
        views.IngredientCreateView.as_view(),
        name="ingredient-create",
    ),
    path(
        "ingredients/<int:pk>/",
        views.IngredientDetailView.as_view(),
        name="ingredient-detail",
    ),
    path(
        "ingredients/update/<int:pk>",
        views.IngredientUpdateView.as_view(),
        name="ingredient-update",
    ),
    path(
        "ingredients/delete/<int:pk>",
        views.IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),
]
