from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
# 초기 상품 데이터 생성하기
  path('get_deposit_products/', views.get_deposit_products),
  path('get_saving_products/', views.get_saving_products),
  
# deposit
  path('deposit/', views.deposit_product_list),
  path('deposit/<str:deposit_code>/', views.deposit_detail),
  path('deposit/<str:deposit_code>/option/', views.deposit_option_list),
  path('bank/deposit/<str:bank_name>/', views.bank_deposit),
  path('like/deposit/<str:deposit_code>/', views.like_deposit),
  path('recommend/deposit/<str:username>/', views.deposit_recommend),
  path('recommend/deposit/second/<str:username>/', views.deposit_recommend_second),

# saving
  path('saving/', views.saving_product_list),
  path('saving/<str:saving_code>/', views.saving_detail),
  path('saving/<str:saving_code>/option/', views.saving_option_list),
  path('bank/saving/<str:bank_name>/', views.bank_saving),
  path('like/saving/<str:saving_code>/', views.like_saving),
  path('recommend/saving/<str:username>/', views.saving_recommend),
  path('recommend/saving/second/<str:username>/', views.saving_recommend_second),
]
