from django.urls import path, include, re_path
from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tables', views.TableViewSet)
router.register('roles', views.RoleViewSet)
router.register('departments', views.DepartmentViewSet)
router.register('meal-categories', views.MealCategoryViewSet)
router.register('meal-categories-by-departments', views.MealCategoriesByDepartmentViewSet)
router.register('statuses', views.StatusViewSet)
router.register('service-percentages', views.ServicePercentageViewSet)
router.register('meals', views.MealViewSet)
router.register('meals-by-categories', views.MealsByCategoryViewSet)
router.register('orders', views.OrderViewSet)
router.register('order-item', views.OrderItemViewSet)
router.register('checks', views.OrderCheckViewSet)
router.register('meals-to-orders', views.MealsToOrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('tables', views.TableViewSet),
    path('roles', views.RoleViewSet),
    path('departments', views.DepartmentViewSet),
    path('meal-categories', views.MealCategoryViewSet),
    path('meal-categories-by-departments', views.MealCategoriesByDepartmentViewSet),
    path('statuses', views.StatusViewSet),
    path('service-percentages', views.ServicePercentageViewSet),
    path('meals', views.MealViewSet),
    path('meals-by-categories', views.MealsByCategoryViewSet),
    path('orders', views.OrderViewSet),
    path('order-item', views.OrderItemViewSet),
    path('checks', views.OrderCheckViewSet),
    path('meals-to-orders', views.MealsToOrderViewSet)
]