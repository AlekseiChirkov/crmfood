from .models import *
from .serializers import *
from django.http import Http404
from rest_framework import status
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError, ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

class TableViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = Table.objects.all()
    serializer_class   = TableSerializer

    def get(self):
        tables     = self.queryset.all()
        serializer = self.serializer_class(tables, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self):
        serializer = self.serializer_class(data=requset.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('table_id is required.')

        try:
            table = self.queryset.get(id=pk)
        except Table.DoesNotExist:
            raise Http404
        else:
            table.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = Role.objects.all()
    serializer_class   = RoleSerializer

    def get(self):
        role       = self.queryset.all()
        serializer = self.serializer_class(role, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('pole_id is required.')

        try:
            role = self.queryset.get(id=pk)
        except Role.DoesNotExist:
            raise Http404
        else:
            role.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = Department.objects.all()
    serializer_class   = DepartmentSerializer

    def get(self):
        departments = self.queryset.all()
        serializer  = self.serializer_class(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('department_id is required.')

        try:
            department = self.queryset.get(id=pk)
        except Department.DoesNotExist:
            raise Http404
        else:
            department.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class MealCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = MealCategory.objects.all()
    serializer_class   = MealCategorySerializer

    def get(self):
        meals       = self.queryset.all()
        serializer  = self.serializer_class(meals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('department_id is required.')

        try:
            meal = self.queryset.get(id=pk)
        except Meal.DoesNotExist:
            raise Http404
        else:
            meal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class MealCategoriesByDepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = MealCategoriesByDepartment.objects.all()
    serializer_class   = MealCategoriesByDepartmentSerializer

    def get(self):
        meal_categories = self.queryset.all()
        serializer      = self.serializer_class(meal_categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('department_id is required.')

        try:
            meal_category = self.queryset.get(id=pk)
        except MealCategoriesByDepartment.DoesNotExist:
            raise Http404
        else:
            meal_category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = Status.objects.all()
    serializer_class   = StatusSerializer

    def get(self):
        statuses        = self.queryset.all()
        serializer      = self.serializer_class(statuses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('department_id is required.')

        try:
            stat = self.queryset.get(id=pk)
        except Status.DoesNotExist:
            raise Http404
        else:
            stat.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
#
class ServicePercentageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = ServicePercentage.objects.all()
    serializer_class   = ServicePercentageSerializer

    def get(self):
        service_perc    = self.queryset.all()
        serializer      = self.serializer_class(service_perc, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('department_id is required.')

        try:
            service = self.queryset.get(id=pk)
        except ServicePercentage.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class MealViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = Meal.objects.all()
    serializer_class   = MealSerializer

    def get(self):
        meals = self.queryset.all()
        serializer = self.serializer_class(meals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('department_id is required.')

        try:
            meal = self.queryset.get(id=pk)
        except Meal.DoesNotExist:
            raise Http404
        else:
            meal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class MealsByCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = MealsByCategory.objects.all()
    serializer_class   = MealsByCategorySerializer

    def get(self):
        meal_by_categories = self.queryset.all()
        serializer      = self.serializer_class(meal_by_categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('department_id is required.')

        try:
            meal_by_category = self.queryset.get(id=pk)
        except MealsByCategory.DoesNotExist:
            raise Http404
        else:
            meal_by_category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = Order.objects.all()
    serializer_class   = OrderSerializer

    def get(self):
        orders = self.queryset.all()
        serializer      = self.serializer_class(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('department_id is required.')

        try:
            order = self.queryset.get(id=pk)
        except Order.DoesNotExist:
            raise Http404
        else:
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = OrderItem.objects.all()
    serializer_class   = OrderItemSerializer

    def get(self):
        order_items = self.queryset.all()
        serializer      = self.serializer_class(order_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('department_id is required.')

        try:
            order_item = self.queryset.get(id=pk)
        except OrderItem.DoesNotExist:
            raise Http404
        else:
            order_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class OrderCheckViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = OrderCheck.objects.all()
    serializer_class   = OrderCheckSerializer

    def get(self):
        order_checks = self.queryset.all()
        serializer      = self.serializer_class(order_checks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('department_id is required.')

        try:
            order_check = self.queryset.get(id=pk)
        except OrderCheck.DoesNotExist:
            raise Http404
        else:
            order_check.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class MealsToOrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset           = MealsToOrder.objects.all()
    serializer_class   = MealsToOrderSerializer

    def get(self):
        meal_to_orders = self.queryset.all()
        serializer      = self.serializer_class(meal_to_orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('department_id is required.')

        try:
            meals_to_order = self.queryset.get(id=pk)
        except MealsToOrder.DoesNotExist:
            raise Http404
        else:
            meals_to_order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class GetSum(APIView):
    queryset         = OrderCheck.objects.all()
    serializer_class = OrderCheckSerializer

    def get(self, request):
        checks     = self.queryset.all()
        serializer = self.serializer_class(checks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
