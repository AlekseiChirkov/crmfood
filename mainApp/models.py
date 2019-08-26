from django.db import models
from datetime import datetime
from django.db.models import Sum
from django.shortcuts import get_object_or_404

class Table(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % (self.name)

class Role(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % (self.name)

class Department(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % (self.name)

class User(models.Model):
    name         = models.CharField(max_length=64)
    surname      = models.CharField(max_length=64)
    login        = models.CharField(max_length=64)
    password     = models.CharField(max_length=64)
    email        = models.EmailField()
    role_id      = models.ForeignKey(Role, on_delete=models.CASCADE)
    date_of_load = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    phone        = models.IntegerField()

    def __str__(self):
        return '%s' % (self.name)

class UserToken(models.Model):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    token   = models.CharField(max_length=128)

    def __str__(self):
        return '%s %s' % (self.role_id, self.token)

class MealCategory(models.Model):
    name          = models.CharField(max_length=64)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)

class MealCategoriesByDepartment(models.Model):
    name          = models.CharField(max_length=64)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.name)

class Status(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%' % (self.name)

class ServicePercentage(models.Model):
    percentage = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.percentage)

class Meal(models.Model):
    name        = models.CharField(max_length=64)
    category_id = models.ForeignKey(MealCategory, on_delete=models.CASCADE, related_name='meals')
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return '%s' % (self.name)

class MealsByCategory(models.Model):
    name        = models.CharField(max_length=64)
    category_id = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return '%s' % (self.name)

class Order(models.Model):
    waiter_id  = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id   = models.ForeignKey(Table, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=64)
    is_it_open = models.BooleanField(default=True)
    date       = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return '%s' % (self.waiter_id)

    def total_sum(self):
        return sum(item.get_sum() for item in self.meals.all())

class OrderItem(models.Model):
    meal  = models.ForeignKey(Meal, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    order = models.ForeignKey(Order, related_name='meals', on_delete=models.CASCADE)

    def get_sum(self):
        return self.count * self.meal.price

class OrderCheck(models.Model):
    order_id    = models.OneToOneField(Order, on_delete=models.CASCADE)
    date        = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    service_fee = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.order_id)

    def fee(self):
        return self.order_id.total_sum() + self.service_fee.percentage

class MealsToOrder(models.Model):
    unique_id = models.AutoField(primary_key=True)
    order_id  = models.ForeignKey(Order, on_delete=models.CASCADE)
    meals     = models.ManyToManyField(Meal)

    def __str__(self):
        return '%' % (self.unique_id)
