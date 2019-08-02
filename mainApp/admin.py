from django.contrib import admin
from .models import *

admin.site.register(Table)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(User)
admin.site.register(UserToken)
admin.site.register(MealCategory)
admin.site.register(MealCategoriesByDepartment)
admin.site.register(Status)
admin.site.register(ServicePercentage)
admin.site.register(Meal)
admin.site.register(MealsByCategory)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderCheck)
admin.site.register(MealsToOrder)
