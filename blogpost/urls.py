from django.urls import path, include
from .views import BlogpostView, AuthorView, LoginView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'post/', BlogpostView, basename='blogpost')
# router.register(r'Author/', AuthorView, basename='author')
# router.register(r'login/', LoginView, basename='login')


urlpatterns = [
    path('', include(router.urls)), 
    path('login/', LoginView.as_view(), name='login'),
    path('author/', AuthorView.as_view(), name='login'),
]
