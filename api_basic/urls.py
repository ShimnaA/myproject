from django.urls import path
from . import views

urlpatterns = [
    path('Authors/', views.article_list),
    path('Authors/<int:pk>', views.article_detail)
]
