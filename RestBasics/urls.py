from django.urls import path, include
# from api_basic.views import article_list, article_detail
from api_basic.views import GenericAPIView


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('generic/detail/<int:id>/', GenericAPIView.as_view()),
]



# urlpatterns = [
#     path('article/', article_list),
#     path('detail/<int:pk>/', article_detail)
# ]
