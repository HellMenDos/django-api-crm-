from django.urls import path
from . import views

urlpatterns = [
    path('api/get/users/all', views.UserApi.as_view(), name=None),
    path('api/get/users/one/<int:num>', views.UserOneApi.as_view(), name=None),
    path('api/post/users/insert', views.UserRegistr.as_view(), name=None),
    path('api/post/users/update', views.UserUpdate.as_view(), name=None),
    path('api/get/deals/all', views.DealApi.as_view(), name=None),
    path('api/get/deals/one/<int:num>', views.DealOneApi.as_view(), name=None),
    path('api/post/deals/insert', views.InsertDealApi.as_view(), name=None),
    path('api/post/deals/delete/<int:num>', views.DeleteDealApi.as_view(), name=None),
    path('api/get/start/one/<int:num>', views.StartOneApi.as_view(), name=None),
    path('api/post/start/insert', views.InsertStartApi.as_view(), name=None),
    path('api/post/start/delete/<int:num>', views.DeleteDealApi.as_view(), name=None),

    path('api/post/user/login/', views.UserLogin.as_view(), name=None),
    path('api/user/activate/<int:num>', views.UserActivate.as_view(), name=None),
]
