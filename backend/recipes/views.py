from rest_framework.generics import RetrieveAPIView, \
    UpdateAPIView, \
    get_object_or_404, CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import LikeSerializer, RecipeSerializer, \
    CommentSerializer, NewRecipeSerializer, EditRecipeSerializer, SearchRecipeSerializer, FavouriteRecipeSerializer, RateRecipeSerializer
from .models import Recipe, Instruction, Ingredient, Diet, Comment, Rate, UploadedIngredient
from rest_framework import generics, serializers
from rest_framework.parsers import MultiPartParser, FormParser


class CreateRecipeView(generics.CreateAPIView):
    serializer_class = RecipeSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        recipe = Recipe.objects.create(
            title=data['title'],
            description=data['description'],
            cuisine=data['cuisine'],
            prep_time=data['prep_time'],
            servings=data['servings'],
            owner_id=request.user.id,
        )

        for ingredient, grams in data['ingredient'].items():
            if not UploadedIngredient.objects.filter(name=ingredient.title()).exists():
                uploaded_ingredient = UploadedIngredient.objects.create(name=ingredient.title())
                Ingredient.objects.create(recipe=recipe, ingredient=uploaded_ingredient, grams=grams)
            else:
                uploaded_ingredient = UploadedIngredient.objects.get(name=ingredient.title())
                Ingredient.objects.create(recipe=recipe, ingredient=uploaded_ingredient, grams=grams)

        for i in range(len(data['instruction'])):
            Instruction.objects.create(num=i, instruction=data['instruction'][i], recipe=recipe)

        for i in data['diet']:
            Diet.objects.create(diet=i, recipe=recipe)

        recipe_serializer = RecipeSerializer(recipe)
        return Response(recipe_serializer.data)


class GetRecipeView(RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        serializer = NewRecipeSerializer(recipe)
        final_dict = serializer.data
        d = []
        print(serializer.data.get('instruction'))
        for i in serializer.data.get('instruction'):
            d.append(Instruction.objects.get(id=i).instruction)
        final_dict['instruction'] = d
        d = []
        for i in serializer.data.get('ingredient'):
            d.append(Ingredient.objects.get(id=i).ingredient)
        final_dict['ingredient'] = d
        d = []
        for i in serializer.data.get('diet'):
            d.append(Diet.objects.get(id=i).diet)
        final_dict['diet'] = d
        d = []
        for i in serializer.data.get('comment'):
            d.append(Comment.objects.get(id=i).comment)
        final_dict['comment'] = d
        final_dict['like'] = len(serializer.data.get('like'))
        count = Rate.objects.filter(recipe=recipe).count()
        x = Rate.objects.filter(recipe=recipe)
        y = 0
        for i in range(len(x)):
            y += x[i].rating
        final_dict['rating'] = 0
        if count > 0:
            final_dict['rating'] = round(y / count, 1)
        return Response(final_dict)


class CreateCommentView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class LikeRecipeView(CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


class EditRecipeView(UpdateAPIView):
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EditRecipeSerializer
    lookup_field = 'id'


class DeleteRecipeView(DestroyAPIView):
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        t = Recipe.objects.filter(id=self.kwargs['recipe_id'])
        if not t.exists():
            raise serializers.ValidationError({"recipe": "This recipe does not exist"})
        if self.request.user != Recipe.objects.get(pk=self.kwargs['recipe_id']).owner:
            raise serializers.ValidationError({"authorize": "You dont have permission to edit this recipe"})
        Recipe.objects.get(id=self.kwargs['recipe_id']).delete()
        return Response({"Success": f"You have successfully deleted the recipe with id {self.kwargs['recipe_id']}"})


class SearchRecipeView(generics.ListCreateAPIView):
    search_fields = ['title', 'owner_name']
    filterset_fields = ['diet', 'ingredient', 'cuisine', 'prep_time']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    queryset = Recipe.objects.all()
    serializer_class = SearchRecipeSerializer
    permission_classes = [AllowAny]


class FavouriteRecipeView(CreateAPIView):
    serializer_class = FavouriteRecipeSerializer
    permission_classes = [IsAuthenticated]


class RateRecipeView(CreateAPIView):
    serializer_class = RateRecipeSerializer
    permission_classes = [IsAuthenticated]