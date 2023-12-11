from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.ManyToManyField('Ingredient', related_name='recipes')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='recipes')
    difficulty_level = models.ForeignKey('DifficultyLevel', on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return f"{self.title} - {self.category.name}"

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.quantity})"

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description[:50]}"  

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField()

    def __str__(self):
        return f"Recenzja {self.user.username} dla {self.recipe.title} - Ocena: {self.rating}"

class DifficultyLevel(models.Model):
    LEVEL_CHOICES = [
        ('1', 'Łatwy'),
        ('2', 'Średni'),
        ('3', 'Zaawansowany'),
    ]
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    def __str__(self):
        return f"Poziom trudności {self.get_level_display()}"  