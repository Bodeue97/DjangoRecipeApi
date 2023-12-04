from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Ingredient
from .serializers import IngredientSerializer, UserRegistrationSerializer



# user register
class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientListView(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientCreateView(generics.CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetailView(generics.RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientUpdateView(generics.UpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDeleteView(generics.DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
