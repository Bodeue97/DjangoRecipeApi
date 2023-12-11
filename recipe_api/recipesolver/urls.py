from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="user-registration"),
    path('api-auth/', include('rest_framework.urls')),

    path("ingredients/", views.IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create/", views.IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/", views.IngredientDetailView.as_view(), name="ingredient-detail"),
    path("ingredients/update/<int:pk>", views.IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredients/delete/<int:pk>", views.IngredientDeleteView.as_view(), name="ingredient-delete"),

    path("recipes/", RecipeListView.as_view(), name="recipe-list"),
    path("recipes/create/", RecipeCreateView.as_view(), name="recipe-create"),
    path("recipes/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    path("recipes/update/<int:pk>", RecipeUpdateView.as_view(), name="recipe-update"),
    path("recipes/delete/<int:pk>", RecipeDeleteView.as_view(), name="recipe-delete"),

    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/create/", CategoryCreateView.as_view(), name="category-create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("categories/update/<int:pk>", CategoryUpdateView.as_view(), name="category-update"),
    path("categories/delete/<int:pk>", CategoryDeleteView.as_view(), name="category-delete"),

    path("reviews/", ReviewListView.as_view(), name="review-list"),
    path("reviews/create/", ReviewCreateView.as_view(), name="review-create"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
    path("reviews/update/<int:pk>", ReviewUpdateView.as_view(), name="review-update"),
    path("reviews/delete/<int:pk>", ReviewDeleteView.as_view(), name="review-delete"),

    path('recipes/by-ingredient/<int:ingredient_id>/', RecipeByIngredientView.as_view(), name='recipes-by-ingredient'),
    path('ingredients/by-recipe/<int:recipe_id>/', IngredientsByRecipeView.as_view(), name='ingredients-by-recipe'),

]
