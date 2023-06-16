from django.urls import path, include
# from api_basic.views import article_list, article_detail
from api_basic.views import ArticleAPIView, ArticleDetail


urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetail.as_view())
]



# urlpatterns = [
#     path('article/', article_list),
#     path('detail/<int:pk>/', article_detail)
# ]
