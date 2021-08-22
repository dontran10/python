from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views
from rest_framework.routers import DefaultRouter

from .views import author, book, category, viewset

urlpatterns = [
    path('categories', category.category_list),
    path('categories/<int:id>', category.category_detail),
    path('authors', author.AuthorAPIView.as_view()),
    path('authors/<int:id>', author.AuthorDetailAPIView.as_view()),
    path('books', book.BookAPIView.as_view()),
    path('books/<int:id>', book.BookDetailAPIView.as_view()),
    path('tokens', authtoken_views.obtain_auth_token),
]

router = DefaultRouter()
router.register(r'books', viewset.BookViewSet)

urlpatterns += [
    path('view-set/', include(router.urls))
]
