
from django.urls import path
#from .import views
from .views import HomeView , ArticleDetailView ,AddPostView ,UpdatePostView , DeletePostView , AddCategoryView, Categoryview , CategoryListview
from graphene_django.views import GraphQLView



urlpatterns = [
    
    #path('',views.home,name='home'),
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name='delete_post'),
    path('add_catgeory/',AddCategoryView.as_view(),name='add_category'),
    #path('catgeory/<str:cats',CategoryView,name='category'),
    path('category/<str:cats>',Categoryview,name='category'),
    path('category-list/',CategoryListview,name='category-list'),
    








]

