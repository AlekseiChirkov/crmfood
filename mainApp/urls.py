from django.urls import path, include, re_path
from . import views
from .views import (
    UserListAPIView,
    UserDetailAPIView,
    UserUpdateAPIView,
    UserDeleteApiView,
    MealListAPIView,
    MealDetailAPIView,
    MealUpdateAPIView,
    MealDeleteAPIView
    )
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tables', views.TableViewSet)
router.register('roles', views.RoleViewSet)
router.register('departments', views.DepartmentViewSet)
router.register('users', views.UserViewSet)
router.register('user-tokens', views.UserTokenViewSet)
router.register('mealcategories', views.MealCategoryViewSet)
router.register('meal-categories-by-departments', views.MealCategoriesByDepartmentViewSet)
router.register('statuses', views.StatusViewSet)
router.register('servisepercentages', views.ServicePercentageViewSet)
router.register('meals', views.MealViewSet)
router.register('meals-by-categories', views.MealsByCategoryViewSet)
router.register('orders', views.OrderViewSet)
router.register('order-item', views.OrderItemViewSet)
router.register('checks', views.OrderCheckViewSet)
router.register('meals-to-orders', views.MealsToOrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^users/$', UserListAPIView.as_view(), name='list'),
    re_path(r'^users/(?P<id>\d+)/$', UserDetailAPIView.as_view(), name='detail'),
    re_path(r'^users/(?P<id>\d+)/edit/$', UserUpdateAPIView.as_view(), name='update'),
    re_path(r'^users/(?P<id>\d+)/delete/$', UserDeleteApiView.as_view(), name='delete'),
    re_path(r'^meals/$', MealListAPIView.as_view(), name='list'),
    re_path(r'^meals/(?P<id>\d+)/$', MealDetailAPIView.as_view(), name='detail'),
    re_path(r'^meals/(?P<id>\d+)/edit/$', MealUpdateAPIView.as_view(), name='update'),
    re_path(r'^meals/(?P<id>\d+)/delete/$', MealDeleteAPIView.as_view(), name='delete')
]
