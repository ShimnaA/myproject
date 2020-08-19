from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Articles/', views.article_list),
    path('Articles/<int:pk>', views.article_detail)
]
urlpatterns = format_suffix_patterns(urlpatterns)
