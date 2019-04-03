from django.urls import path
from .views import (
    BlogListView, 
    BlogDetailView, 
    BlogCreateView,     # ссылка на создание
    BlogUpdateView,     # сслыка на обновление
    BlogDeleteView,     # сслыка на удаление
)

urlpatterns = [
    path('post/<int:pk>/edit/', 
        BlogUpdateView.as_view(), name='post_edit'),                    # new 4
    path('post/<int:pk>/delete/',
        BlogDeleteView.as_view(), name='post_delete'),                  # new 5 
    path('post/new/', BlogCreateView.as_view(), name='post_new'),           # new 3 сслыка для создания поста
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail' ), # new 2 ссылка для детализации поста (зайти в пост)
    path('', BlogListView.as_view(), name='home'),  # new 1 ссылка для отображения начатльной страницы с потами
]