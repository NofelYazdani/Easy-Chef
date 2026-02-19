from rest_framework.generics import RetrieveAPIView, get_object_or_404, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from recipes.models import ShoppingList, Ingredient, Recipe, Favourite, Like, Comment, Rate
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, NewUserSerializer, EditProfileSerializer, ShoppingListSerializer
from rest_framework import generics
User = get_user_model()


# Create your views here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class GetProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=self.request.user.id)
        serializer = NewUserSerializer(user)
        return Response(serializer.data)


class EditProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EditProfileSerializer


class ShoppingListView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class GetShoppingListView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        final_dict = {"Recipes": [], "Total": {}}
        shopping_list = ShoppingList.objects.filter(owner=request.user)
        visited = {}
        for i in list(shopping_list):
            final_dict["Recipes"].append(i.recipe.title)
            print(i.recipe.title)
            temp = Ingredient.objects.filter(recipe=i.recipe)
            print(i.recipe.id)
            print(list(temp))
            for k in list(temp):
                print(k.ingredient.name)
                if k.ingredient.name not in visited.keys():
                    visited[k.ingredient.name] = int(k.grams)
                else:
                    visited[k.ingredient.name] += int(k.grams)
        final_dict["Total"] = visited
        return Response(final_dict)


class MyRecipesView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        recipes_created = []
        for i in list(Recipe.objects.filter(owner=request.user)):
            recipes_created.append((i.id, i.title))

        recipes_fav = []
        for i in list(Favourite.objects.filter(owner=request.user)):
            recipes_fav.append((i.recipe.id, i.recipe.title))

        recipes_liked = []
        for i in list(Like.objects.filter(owner=request.user)):
            recipes_liked.append((i.recipe.id, i.recipe.title))

        recipes_commented = set({})
        for i in list(Comment.objects.filter(owner=request.user)):
            recipes_commented.add((i.recipe.id, i.recipe.title))

        recipes_rate = []
        for i in list(Rate.objects.filter(owner=request.user)):
            recipes_rate.append((i.recipe.id, i.recipe.title))

        return Response({
            "Recipes created": recipes_created,
            "Recipes favourited": recipes_fav,
            "Recipes liked": recipes_liked,
            "Recipes commented on": recipes_commented,
            "Recipes rated": recipes_rate
        })







