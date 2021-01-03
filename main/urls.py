from django.urls import path
from . import views

urlpatterns = [
    path('api/get/users/all', views.UserListView.as_view(), name=None),
    path('api/get/users/one/<int:num>', views.UserOneListView.as_view(), name=None),
    path('api/post/users/insert', views.InsertListView.as_view(), name=None),
    path('api/get/deals/all', views.DealListView.as_view(), name=None),
    path('api/get/deals/one/<int:num>', views.DealOneListView.as_view(), name=None),
    path('api/post/deals/insert', views.InsertDealListView.as_view(), name=None),
    path('api/post/deals/delete/<int:num>', views.DeleteDealListView.as_view(), name=None),
    path('api/get/start/one/<int:num>', views.StartOneListView.as_view(), name=None),
    path('api/post/start/insert', views.InsertStartListView.as_view(), name=None),
    path('api/post/start/delete/<int:num>', views.DeleteDealListView.as_view(), name=None),
]
