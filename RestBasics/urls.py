from django.urls import path, include
from api_basic.views import article_list, article_detail


urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>/', article_detail)
]
