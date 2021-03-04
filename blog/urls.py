from django.urls import path
from blog import views

urlpatterns = [
    path('',views.bloghome,name="bloghome"),
    path('addBlog/',views.addBlog,name="addBlog"),
    path('writeBlog/',views.writeBlog,name="writeBlog"),
    path('addingBlog/',views.handleAddBlog,name="handleAddBlog"),
    path('<str:slug>',views.blogPost,name="blogPost"),
    path('deleteUserBlog/',views.deleteUserBlog,name="deleteUserBlog"),
    path('EditUserBlog/',views.EditUserBlog,name="EditUserBlog"),
    path('handleEditUserBlog/',views.handleEditUserBlog,name="handleEditUserBlog"),
    
    path('search/',views.search,name="search"),
]