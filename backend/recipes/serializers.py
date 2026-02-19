from rest_framework import serializers
from .models import Recipe, Instruction, Ingredient, Diet, Comment, Like, Favourite, Rate, UploadedIngredient
import re


class UploadedIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedIngredient
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    ingredient = UploadedIngredientSerializer()
    class Meta:
        model = Ingredient
        fields = '__all__'

class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'

class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=True, read_only=True)
    diet = DietSerializer(many=True, read_only=True)
    instruction = InstructionSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'cuisine', 'prep_time', 'servings', 'instruction', 'ingredient', 'diet']


class CommentSerializer(serializers.ModelSerializer):
    recipe = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField()
    time = serializers.ReadOnlyField(required=False)

    class Meta:
        model = Comment
        fields = ['owner', 'time', 'recipe', 'comment']

    def create(self, validated_data):
        if not Recipe.objects.filter(id=self.context.get('view').kwargs.get('recipe_id')).exists():
            raise serializers.ValidationError({"recipe": "Recipe does not exist"})
        Comment.objects.create(owner=self.context['request'].user,
                               recipe=Recipe.objects.get(id=self.context.get('view').kwargs.get('recipe_id')),
                               comment=validated_data['comment'])
        return validated_data


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['owner', 'recipe']

        extra_kwargs = {
            'owner': {'required': False},
            'recipe': {'required': False}
        }

    def create(self, validated_data):
        if not Recipe.objects.filter(id=self.context.get('view').kwargs.get('recipe_id')).exists():
            raise serializers.ValidationError({"like": "Recipe does not exist"})

        if Like.objects.filter(recipe=self.context.get('view').kwargs.get('recipe_id'),
                               owner=self.context['request'].user).exists():
            Like.objects.filter(recipe=self.context.get('view').kwargs.get('recipe_id'),
                                     owner=self.context['request'].user).delete()
            return {"like": "You have successfully un-liked this recipe"}

        Like.objects.create(owner=self.context['request'].user,
                            recipe=Recipe.objects.get(id=self.context.get('view').kwargs.get('recipe_id')))

        validated_data["success"] = "You have successfully liked this recipe"
        return validated_data

    def to_representation(self, instance):
        return {"Like": "You have successfully liked this post"}


class NewRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'owner_name', 'title', 'description', 'cuisine', 'image',
                  'prep_time', 'servings', 'instruction', 'ingredient', 'diet', 'comment', 'like', 'rating']


class EditRecipeSerializer(serializers.ModelSerializer):
    instruction = serializers.CharField(max_length=255, required=False)
    ingredient = serializers.CharField(max_length=255, required=False)
    diet = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cuisine',
                  'prep_time', 'servings', 'instruction', 'ingredient', 'diet']
        extra_kwargs = {
            'title': {'required': False},
            'description': {'required': False},
            'cuisine': {'required': False},
            'prep_time': {'required': False},
            'servings': {'required': False},
            'instruction': {'required': False},
            'ingredient': {'required': False},
            'diet': {'required': False},

        }

    def validate(self, attrs):
        DIET_CHOICES = ['Halal', 'Kosher', 'Vegan', 'Vegetarian', 'Gluten-Free', 'Dairy-Free', 'Keto', 'Carnivore', 'Pescatarian']
        if 'diet' in attrs and attrs['diet'] not in DIET_CHOICES:
            raise serializers.ValidationError({"diet": "Please pick from one of the following: Halal, Kosher, Vegetarian, Gluten-Free, Dairy-Free, Keto, Carnivore, Pescatarian"})
        return attrs

    def update(self, instance, validated_data):
        # https://medium.com/django-rest/django-rest-framework-change-password-and-update-profile-1db0c144c0a3
        pattern = r"^\d+g of [a-zA-Z ]+$"
        user = self.context['request'].user
        if user != Recipe.objects.get(pk=self.context.get('view').kwargs.get('id')).owner:
            raise serializers.ValidationError({"authorize": "You dont have permission to edit this recipe"})

        d = dict(self.initial_data).get('instruction')
        d2 = dict(self.initial_data).get('ingredient')
        d3 = dict(self.initial_data).get('diet')

        temp = Recipe.objects.get(pk=self.context.get('view').kwargs.get('id'))
        if 'title' in validated_data and len(validated_data['title']) != 0:
            temp.title = validated_data['title']
        if 'description' in validated_data and len(validated_data['description']) != 0:
            temp.description = validated_data['description']
        if 'cuisine' in validated_data and len(validated_data['cuisine']) != 0:
            temp.cuisine = validated_data['cuisine']
        if 'prep_time' in validated_data and len(validated_data['prep_time']) != 0:
            temp.prep_time = validated_data['prep_time']
        if 'servings' in validated_data and len(validated_data['servings']) != 0:
            temp.servings = validated_data['servings']
        if 'instruction' in validated_data and len(d) != 0:
            Instruction.objects.filter(recipe=temp).delete()
            for i in d:
                Instruction.objects.create(instruction=i, recipe=temp)
        if 'ingredient' in validated_data and len(d2) != 0:
            Ingredient.objects.filter(recipe=temp).delete()
            for i in d2:
                match = re.search(pattern, i)
                if match:
                    Ingredient.objects.create(ingredient=i, recipe=temp)
                else:
                    raise serializers.ValidationError({"ingredient format": "Please follow the following format for ingredients: {Number}g of {Ingredient}"})
        if 'diet' in validated_data and len(d3) != 0:
            Diet.objects.filter(recipe=temp).delete()
            for i in d3:
                Diet.objects.create(diet=i, recipe=temp)
        # temp.save()
        validated_data['instruction'] = d
        validated_data['ingredient'] = d2
        validated_data['diet'] = d3
        temp.save()
        return validated_data

class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ['instruction']


class DefaultCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = ['diet']

class SearchRecipeSerializer(serializers.ModelSerializer):
    instruction = serializers.SerializerMethodField(read_only=True)
    ingredient = serializers.SerializerMethodField(read_only=True)
    comment = serializers.SerializerMethodField(read_only=True)
    diet = serializers.SerializerMethodField(read_only=True)
    like = serializers.SerializerMethodField(read_only=True)
    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Recipe
        fields = ['owner_name', 'title', 'description', 'cuisine', 'image',
                  'prep_time', 'servings', 'instruction', 'ingredient', 'diet', 'comment', 'like', 'rating']

    def get_instruction(self, obj):
        d = []
        for i in range(len(InstructionSerializer(obj.instruction, many=True).data)):
            d.append(InstructionSerializer(obj.instruction, many=True).data[i].popitem()[1])
        return d

    def get_ingredient(self, obj):
        d = []
        for i in range(len(IngredientSerializer(obj.ingredient, many=True).data)):
            d.append(IngredientSerializer(obj.ingredient, many=True).data[i].popitem()[1])
        return d

    def get_comment(self, obj):
        d = []
        for i in range(len(DefaultCommentSerializer(obj.comment, many=True).data)):
            d.append(DefaultCommentSerializer(obj.comment, many=True).data[i].popitem()[1])
        return d

    def get_diet(self, obj):
        d = []
        for i in range(len(DietSerializer(obj.diet, many=True).data)):
            d.append(DietSerializer(obj.diet, many=True).data[i].popitem()[1])
        return d

    def get_like(self, obj):
        return Like.objects.filter(recipe=obj).count()

    def get_rating(self, obj):
        c, t = Rate.objects.filter(recipe=obj).count(), 0
        for i in Rate.objects.filter(recipe=obj):
            t += i.rating
        if c != 0:
            return round(t / c, 1)
        return 0


class FavouriteRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = '__all__'
        read_only_fields = ('owner', 'recipe',)

        extra_kwargs = {
            'owner': {'required': False, 'read_only':False},
            'recipe': {'required': False, 'read_only':False}
        }

    def create(self, validated_data):
        if not Recipe.objects.filter(id=self.context.get('view').kwargs.get('recipe_id')).exists():
            raise serializers.ValidationError({"favourite": "Recipe does not exist"})

        if Favourite.objects.filter(recipe=self.context.get('view').kwargs.get('recipe_id'),
                               owner=self.context['request'].user).exists():
            Favourite.objects.filter(recipe=self.context.get('view').kwargs.get('recipe_id'),
                                  owner=self.context['request'].user).delete()
            return {"succcess": "Success"}

        Favourite.objects.create(owner=self.context['request'].user,
                            recipe=Recipe.objects.get(id=self.context.get('view').kwargs.get('recipe_id')))

        return validated_data

    def to_representation(self, instance):
        if Favourite.objects.filter(recipe=self.context.get('view').kwargs.get('recipe_id'),
                                       owner=self.context['request'].user).exists():
            return {"Favourite": "You have successfully favourited this recipe"}
        return {"Favourite": "You have successfully un-favourited this recipe"}


class RateRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'
        read_only_fields = ('owner', 'recipe',)

        extra_kwargs = {
            'owner': {'required': False, 'read_only':False},
            'recipe': {'required': False, 'read_only':False},
            'rating': {'required': True},
        }

    def create(self, validated_data):
        if not Recipe.objects.filter(
                id=self.context.get('view').kwargs.get('recipe_id')).exists():
            raise serializers.ValidationError({"rate": "Recipe does not exist"})

        if Rate.objects.filter(
                recipe=self.context.get('view').kwargs.get('recipe_id'),
                owner=self.context['request'].user).exists():
            Rate.objects.filter(
                recipe=self.context.get('view').kwargs.get('recipe_id'),
                owner=self.context['request'].user).delete()
            if validated_data['rating'] not in [1, 2, 3, 4, 5]:
                raise serializers.ValidationError(
                    {"rate": "Please pick a rating from 1 - 5"})
            Rate.objects.create(owner=self.context['request'].user,
                                recipe=Recipe.objects.get(id=self.context.get('view').kwargs.get('recipe_id')),
                                rating=validated_data['rating'])
            return validated_data

        if validated_data['rating'] not in [1, 2, 3, 4, 5]:
            raise serializers.ValidationError(
                {"rate": "Please pick a rating from 1 - 5"})
        Rate.objects.create(owner=self.context['request'].user,
                            recipe=Recipe.objects.get(id=self.context.get('view').kwargs.get('recipe_id')),
                            rating=validated_data['rating'])
        return validated_data

    def to_representation(self, instance):
        return {"Rate": f"You have given this recipe a rating of {instance['rating']}"}
