from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all, name="all"),
    path('new', views.create_article, name="new"),
    path('<int:pk>', views.ArticleDetailView.as_view(), name="article_detail"),
    path('<int:pk>/update', views.ArticleUpdateView.as_view(), name="article_update"),
    path('<int:pk>/delete', views.ArticleDeleteView.as_view(), name="article_delete"),
]
