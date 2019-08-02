from rest_framework import serializers
from .models import *

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Table
        fields = ('id', 'name')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Role
        fields = ('id', 'name')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Department
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ('id', 'name', 'surname', 'login', 'password',
                  'email', 'role_id', 'date_of_load', 'phone')

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserToken
        fields = ('role_id', 'token')

class MealCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = MealCategory
        fields = ('id', 'name', 'department_id')

class MealCategoriesByDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MealCategoriesByDepartment
        fields = ('id', 'name', 'department_id')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Status
        fields = ('id', 'name')

class ServicePercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ServicePercentage
        fields = ('percentage',)

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Meal
        fields = ('id', 'name', 'category_id', 'price', 'description')

class MealsByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = MealsByCategory
        fields = ('id', 'name', 'category_id', 'price', 'description')

class OrderSerializer(serializers.ModelSerializer):
    # meal = MealSerializer(many=True)
    total_price = serializers.FloatField(source='total_sum', max_value=None, min_value=None, required=False)
    class Meta:
        model  = Order
        fields = ('id', 'waiter_id', 'table_id', 'table_name',
                  'is_it_open', 'date', 'total_price', 'meals')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = OrderItem
        fields = ('id', 'meal', 'count', 'order')

class OrderCheckSerializer(serializers.ModelSerializer):
    total_price = serializers.FloatField(source='fee', max_value=None, min_value=None, required=False)
    class Meta:
        model  = OrderCheck
        fields = ('id', 'order_id', 'date', 'service_fee', 'total_price')

class MealsToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MealsToOrder
        fields = ('unique_id', 'order_id', 'meals')
