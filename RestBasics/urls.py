from django.urls import path, include
# from api_basic.views import article_list, article_detail
from api_basic.views import ArticleViewSet
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('', include('api_basic.urls'))
    # path('generic/detail/<int:id>/', GenericAPIView.as_view()),
]



# urlpatterns = [
#     path('article/', article_list),
#     path('detail/<int:pk>/', article_detail)
# ]
