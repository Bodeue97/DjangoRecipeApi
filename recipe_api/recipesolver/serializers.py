from rest_framework import serializers
from .models import Recipe, Ingredient, Category, Review, DifficultyLevel
from django.contrib.auth.models import User


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifficultyLevel
        fields = "__all__"


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    category = CategorySerializer()
    difficulty_level = DifficultyLevelSerializer()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "email")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
