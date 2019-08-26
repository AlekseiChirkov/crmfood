import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.response import Response

from mainApp.models import *

class TableTest(TestCase):
    def setUp(self):
        self.table = Table.objects.create(name='Table #1')

    def test_table_name(self):
        get_table = Table.objects.get(
            name='Table #1'
        )
        self.assertEqual(get_table, self.table)

    def test_code_status(self):
        return Response(self.table, status=status.HTTP_201_CREATED)

class RoleTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name='Waiter')

    def test_role_name(self):
        get_role = Role.objects.get(
            name='Waiter'
        )
        self.assertEqual(get_role, self.role)

    def test_code_status(self):
        return Response(self.role, status=status.HTTP_201_CREATED)

class DepartmentTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name='Kitchen')

    def test_department_name(self):
        get_department = Department.objects.get(
            name='Kitchen'
        )
        self.assertEqual(get_department, self.department)

    def test_code_status(self):
        return Response(self.department, status=status.HTTP_201_CREATED)

class UserTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name='Waiter')
        self.user = User.objects.create(
            name='Alex',
            surname='Chirkov',
            login='Scareface',
            password='Password',
            email='tektonik_boy98@mail.ru',
            role_id=self.role,
            phone='0559129557'
        )

    def test_user_name(self):
        get_user = User.objects.get(
            name='Alex',
            surname='Chirkov',
            login='Scareface',
            password='Password',
            email='tektonik_boy98@mail.ru',
            role_id=self.role,
            phone='0559129557'
        )
        self.assertEqual(get_user, self.user)

    def test_code_status(self):
        return Response(self.user, status=status.HTTP_201_CREATED)

class UserTokenTest(TestCase):
    def setUp(self):
        self.role       = Role.objects.create(name='Waiter')
        self.user_token = UserToken.objects.create(
            role_id=self.role,
            token='oisvd1w8v98u89uvu8u2s0v820v0sdi'
        )

    def test_user_token(self):
        get_user_token = UserToken.objects.get(
            role_id=self.role,
            token='oisvd1w8v98u89uvu8u2s0v820v0sdi'
        )
        self.assertEqual(get_user_token, self.user_token)

    def test_code_status(self):
        return Response(self.user_token, status=status.HTTP_201_CREATED)

class MealCategoryTest(TestCase):
    def setUp(self):
        self.department_id = Department.objects.create(name='Kitchen')
        self.meal_category = MealCategory.objects.create(
            name='Pervoe',
            department_id=self.department_id
        )

    def test_meal_category(self):
        get_meal_category = MealCategory.objects.get(
            name='Pervoe',
            department_id=self.department_id
        )
        self.assertEqual(get_meal_category, self.meal_category)

    def test_code_status(self):
        return Response(self.meal_category, status=status.HTTP_201_CREATED)

class MealCategoriesByDepartmentTest(TestCase):
    def setUp(self):
        self.department_id      = Department.objects.create(name='Kitchen')
        self.meal_by_department = MealCategoriesByDepartment.objects.create(
            name='Pervoe',
            department_id=self.department_id
        )

    def test_meal_by_department(self):
        get_meal_by_department = MealCategoriesByDepartment.objects.get(
            name='Pervoe',
            department_id=self.department_id
        )
        self.assertEqual(get_meal_by_department, self.meal_by_department)

    def test_code_status(self):
        return Response(self.meal_by_department, status=status.HTTP_201_CREATED)

class StatusTest(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name='Active')

    def test_status(self):
        get_status = Status.objects.get(name='Active')
        self.assertEqual(get_status, self.status)

    def test_code_status(self):
        return Response(self.status, status=status.HTTP_201_CREATED)

class ServicePercentageTest(TestCase):
    def setUp(self):
        self.service_percentage = ServicePercentage.objects.create(percentage='34')

    def test_service_percentage(self):
        get_service_percentage = ServicePercentage.objects.get(percentage='34')
        self.assertEqual(get_service_percentage, self.service_percentage)

    def test_code_status(self):
        return Response(self.service_percentage, status=status.HTTP_201_CREATED)

class MealTest(TestCase):
    def setUp(self):
        self.department    = Department.objects.create(name='Kitchen')
        self.meal_category = MealCategory.objects.create(
            name='Pervoe',
            department_id=self.department
        )
        self.meal          = Meal.objects.create(
            name='Plov',
            category_id=self.meal_category,
            price='12.95',
            description='Description'
        )

    def test_meal(self):
        get_meal = Meal.objects.get(
            name='Plov',
            category_id=self.meal_category,
            price='12.95',
            description='Description'
        )
        self.assertEqual(get_meal, self.meal)

    def test_code_status(self):
        return Response(self.meal, status=status.HTTP_201_CREATED)

class MealsByCategpryTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name='Kitchen')
        self.meal_category = MealCategory.objects.create(
            name='Pervoe',
            department_id=self.department
        )
        self.meals_by_category = MealsByCategory.objects.create(
            name='Plov',
            category_id=self.meal_category,
            price='12.95',
            description='Description'
        )

    def test_meal_by_category(self):
        get_meal_by_category = MealsByCategory.objects.get(
            name='Plov',
            category_id=self.meal_category,
            price='12.95',
            description='Description'
        )
        self.assertEqual(get_meal_by_category, self.meals_by_category)

    def test_code_status(self):
        return Response(self.meals_by_category, status=status.HTTP_201_CREATED)

class OrderTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name='Waiter')
        self.user = User.objects.create(
            name='Alex',
            surname='Chirkov',
            login='Scareface',
            password='Password',
            email='tektonik_boy98@mail.ru',
            role_id=self.role,
            phone='0559129557'
        )
        self.table = Table.objects.create(
            name='Table #1'
        )
        self.order = Order.objects.create(
            waiter_id=self.user,
            table_id=self.table,
            table_name='Table #1',
            is_it_open=True
        )

    def test_order(self):
        get_order = Order.objects.get(
            waiter_id=self.user,
            table_id=self.table,
            table_name='Table #1',
            is_it_open=True
        )
        self.assertEqual(get_order, self.order)

    def test_code_status(self):
        return Response(self.order, status=status.HTTP_201_CREATED)

class OrderItemTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name='Waiter')
        self.user = User.objects.create(
            name='Alex',
            surname='Chirkov',
            login='Scareface',
            password='Password',
            email='tektonik_boy98@mail.ru',
            role_id=self.role,
            phone='0559129557'
        )
        self.table = Table.objects.create(
            name='Table #1'
        )
        self.order = Order.objects.create(
            waiter_id=self.user,
            table_id=self.table,
            table_name='Table #1',
            is_it_open=True
        )
        self.department    = Department.objects.create(name='Kitchen')
        self.meal_category = MealCategory.objects.create(
            name='Pervoe',
            department_id=self.department
        )
        self.meal = Meal.objects.create(
            name='Plov',
            category_id=self.meal_category,
            price='12.95',
            description='Description'
        )
        self.order_item = OrderItem.objects.create(
            meal=self.meal,
            count='1',
            order=self.order
        )

    def test_order_item(self):
        get_order_item = OrderItem.objects.get(
            meal=self.meal,
            count='1',
            order=self.order
        )
        self.assertEqual(get_order_item, self.order_item)

    def test_code_status(self):
        return Response(self.order_item, status=status.HTTP_201_CREATED)

class OrderCheckTest(TestCase):
    def setUp(self):
        self.service_percentage = ServicePercentage.objects.create(percentage='34')
        self.role               = Role.objects.create(name='Waiter')
        self.user               = User.objects.create(
            name='Alex',
            surname='Chirkov',
            login='Scareface',
            password='Password',
            email='tektonik_boy98@mail.ru',
            role_id=self.role,
            phone='0559129557'
        )
        self.table = Table.objects.create(
            name='Table #1'
        )
        self.order = Order.objects.create(
            waiter_id=self.user,
            table_id=self.table,
            table_name='Table #1',
            is_it_open=True
        )
        self.order_check = OrderCheck.objects.create(
            order_id=self.order,
            service_fee=self.service_percentage
        )

    def test_order_check(self):
        get_order_check = OrderCheck.objects.get(
            order_id=self.order,
            service_fee=self.service_percentage
        )
        self.assertEqual(get_order_check, self.order_check)

    def test_code_status(self):
        return Response(self.order_check, status=status.HTTP_201_CREATED)

class MealsToOrderTest(TestCase):
    def setUp(self):
        self.department    = Department.objects.create(name='Kitchen')
        self.meal_category = MealCategory.objects.create(
            name='Pervoe',
            department_id=self.department
        )
        self.meal = Meal.objects.create(
            name='Plov',
            category_id=self.meal_category,
            price='12.95',
            description='Description'
        )
        self.service_percentage = ServicePercentage.objects.create(percentage='34')
        self.role               = Role.objects.create(name='Waiter')
        self.user               = User.objects.create(
            name='Alex',
            surname='Chirkov',
            login='Scareface',
            password='Password',
            email='tektonik_boy98@mail.ru',
            role_id=self.role,
            phone='0559129557'
        )
        self.table = Table.objects.create(
            name='Table #1'
        )
        self.order = Order.objects.create(
            waiter_id=self.user,
            table_id=self.table,
            table_name='Table #1',
            is_it_open=True
        )
        self.meals_to_order = MealsToOrder.objects.create(
            order_id=self.order
        )

    def test_meal_to_order(self):
        get_meal_to_order = MealsToOrder.objects.get(
            order_id=self.order
        )
        self.assertEqual(get_meal_to_order, self.meals_to_order)

    def test_code_status(self):
        return Response(self.meals_to_order, status=status.HTTP_201_CREATED)