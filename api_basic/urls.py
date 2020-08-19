from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Articles/', views.ArticleList.as_view()),
    path('Articles/<int:pk>', views.ArticleDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
