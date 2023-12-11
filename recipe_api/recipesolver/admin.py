from django.contrib import admin
from .models import Recipe, Ingredient, Category, Review, DifficultyLevel

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recipe._meta.fields]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ingredient._meta.fields]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]  

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Review._meta.fields] 

@admin.register(DifficultyLevel)
class DifficultyLevelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DifficultyLevel._meta.fields] 
