from django.urls import path
from rest_framework.routers import SimpleRouter
#from .views import UserList, UserDetail, PostList, PostDetail
from .views import UserViewSet, PostViewSet

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
#     path('user/',UserList.as_view()),
#     path('user/<int:pk>/',UserDetail.as_view()),
# ]

router = SimpleRouter()
router.register('user', UserViewSet, basename='user')
router.register('', PostViewSet, basename='post')

urlpatterns = router.urls

