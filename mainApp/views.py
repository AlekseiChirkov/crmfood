from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
    )
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from django.db.models import Sum
from django.views.generic.list import ListView

class TableViewSet(viewsets.ModelViewSet):
    queryset         = Table.objects.all()
    serializer_class = TableSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            table = Table.objects.get(pk=pk)
        except Table.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # if request.method == 'GET':
        #     serializer = TableSerializer(table)
        #     return Response(serializer.data)
        # elif request.method == 'PUT':
        #     serializer = TableSerializer(table, data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            table.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class RoleViewSet(viewsets.ModelViewSet):
    queryset         = Role.objects.all()
    serializer_class = RoleSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            role = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            role.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset         = Department.objects.all()
    serializer_class = DepartmentSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            department.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ModelViewSet):
    queryset         = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['delete', 'put', 'get'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class UserListAPIView(ListAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(RetrieveAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    lookup_field     = 'id'

class UserUpdateAPIView(UpdateAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    lookup_field     = 'id'

class UserDeleteApiView(DestroyAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    lookup_field     = 'id'

class UserTokenViewSet(viewsets.ModelViewSet):
    queryset         = UserToken.objects.all()
    serializer_class = UserTokenSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            user_token = UserToken.objects.get(pk=pk)
        except UserToken.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            user_token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class MealCategoryViewSet(viewsets.ModelViewSet):
    queryset         = MealCategory.objects.all()
    serializer_class = MealCategorySerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            meal_category = MealCategory.objects.get(pk=pk)
        except MealCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method =='DELETE':
            meal_category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class MealCategoriesByDepartmentViewSet(viewsets.ModelViewSet):
    queryset         = MealCategoriesByDepartment.objects.all()
    serializer_class = MealCategoriesByDepartmentSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            meal_categories_by_department = MealCategoriesByDepartment.objects.get(pk=pk)
        except MealCategoriesByDepartment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            meal_categories_by_department.delete()
            return Request(status=status.HTTP_204_NO_CONTENT)

class StatusViewSet(viewsets.ModelViewSet):
    queryset         = Status.objects.all()
    serializer_class = StatusSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            statuses = Status.objects.get(pk=pk)
        except Status.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            statuses.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class ServicePercentageViewSet(viewsets.ModelViewSet):
    queryset         = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            service = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            service.delete()
            return Request(status=status.HTTP_204_NO_CONTENT)

class MealViewSet(viewsets.ModelViewSet):
    queryset         = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            meal = Meal.objects.get(pk=pk)
        except Meal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            meal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class MealListAPIView(ListAPIView):
    queryset         = Meal.objects.all()
    serializer_class = MealSerializer

class MealDetailAPIView(RetrieveAPIView):
    queryset         = Meal.objects.all()
    serializer_class = MealSerializer
    lookup_field     = 'id'

class MealUpdateAPIView(UpdateAPIView):
    queryset         = Meal.objects.all()
    serializer_class = MealSerializer
    lookup_field     = 'id'

class MealDeleteAPIView(DestroyAPIView):
    queryset         = Meal.objects.all()
    serializer_class = MealSerializer
    lookup_field     = 'id'

class MealsByCategoryViewSet(viewsets.ModelViewSet):
    queryset         = MealsByCategory.objects.all()
    serializer_class = MealsByCategorySerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            meals_by_category = MealsByCategory.objects.get(pk=pk)
        except MealsByCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            meals_by_category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class OrderViewSet(viewsets.ModelViewSet):
    queryset         = Order.objects.all()
    serializer_class = OrderSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            order = Order.objects.get(pk=pk)
        except Objects.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset         = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            order_item = OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            order_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class OrderCheckViewSet(viewsets.ModelViewSet):
    queryset         = OrderCheck.objects.all()
    serializer_class = OrderCheckSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            check = OrderCheck.objects.get(pk=pk)
        except OrderCheck.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            check.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class MealsToOrderViewSet(viewsets.ModelViewSet):
    queryset         = MealsToOrder.objects.all()
    serializer_class = MealsToOrderSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        pk = request.data.get('id')
        try:
            meals_to_order = MealsToOrder.objects.get(pk=pk)
        except MealsToOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            meals_to_order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class GetSum(APIView):
    queryset         = OrderCheck.objects.all()
    serializer_class = OrderCheckSerializer

    def get(self, request):
        checks     = self.queryset.all()
        serializer = self.serializer_class(checks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
