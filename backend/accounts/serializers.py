from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from recipes.models import ShoppingList, Recipe
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField()
    password2 = serializers.CharField(write_only=True, required=True)
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['password','password2', 'avatar',
                  'email', 'first_name', 'last_name', 'phone']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
            'avatar': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
        )
        if 'avatar' in validated_data.keys():
            user.avatar = validated_data['avatar']
        user.set_password(validated_data['password'])
        user.save()

        return user


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name',
                  'last_name', 'email', 'phone', 'avatar']


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['phone', 'password']
        extra_kwargs = {
            'phone': {'required': True, 'validators':[]},
            'password': {'write_only': True, 'required': True}
        }

    def validate(self, attrs):
        if not authenticate(username=attrs['phone'], password=attrs['password']):
            raise serializers.ValidationError({"phone": "Phone number or password is invalid", "password": "Phone number or password is invalid"})
        return attrs


class EditProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())], required=False)
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'avatar']
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': False},
            'phone': {'required': False},
            'avatar': {'required': False}
        }

    def update(self, instance, validated_data):
        # https://medium.com/django-rest/django-rest-framework-change-password-and-update-profile-1db0c144c0a3
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})


        if 'first_name' in validated_data.keys():
            instance.first_name = validated_data['first_name']
        if 'last_name' in validated_data.keys():
            instance.last_name = validated_data['last_name']
        if 'email' in validated_data.keys():
            instance.email = validated_data['email']
        if 'phone' in validated_data.keys():
            instance.phone = validated_data['phone']
        if 'avatar' in validated_data.keys():
            instance.avatar = validated_data['avatar']

        instance.save()
        return instance


class ShoppingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingList
        fields = ['owner', 'recipe']

        extra_kwargs = {
            'owner': {'required': False},
            'recipe': {'required': False}
        }

    def create(self, validated_data):
        if not Recipe.objects.filter(id=self.context.get('view').kwargs.get('recipe_id')).exists():
            raise serializers.ValidationError({"like": "Recipe does not exist"})

        if ShoppingList.objects.filter(recipe=self.context.get('view').kwargs.get('recipe_id'),
                               owner=self.context['request'].user).exists():
            ShoppingList.objects.filter(recipe=self.context.get('view').kwargs.get('recipe_id'),
                                owner=self.context['request'].user).delete()
            return {"Shopping List": "You have successfully removed this recipe from your shopping list"}

        ShoppingList.objects.create(owner=self.context['request'].user,
                            recipe=Recipe.objects.get(id=self.context.get('view').kwargs.get('recipe_id')))


        return {"Success": "You have successfully added this recipe to your shopping list"}

    def to_representation(self, instance):
        if ShoppingList.objects.filter(recipe=self.context.get('view').kwargs.get('recipe_id'),
                                       owner=self.context['request'].user).exists():
            return {"Shopping List": "You have successfully added this recipe to your shopping list"}
        return {"Shopping List": "You have successfully removed this recipe from your shopping list"}


