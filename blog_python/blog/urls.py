from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('blogs/<blog_id>', views.blogs, name = 'blogs'),
    path('blog_create', views.blog_create, name = 'blog_create'),
    path('blog_update/<blog_id>', views.blog_update, name = 'blog_update'),
    path('blog_delete/<blog_id>', views.blog_delete, name = 'blog_delete'),
    path('comment_delete/<blog_id>/<comment_id>', views.comment_delete, name = 'comment_delete'),
    path('search', views.search, name = 'search'),
    path('register', views.register, name = 'register'),
    path('login', views.loginpage, name = 'loginpage'),
    path('logout', views.logoutpage, name = 'logoutpage'),
    path('login_user', views.login_user, name = 'login_user'),
    path('author_blogs/<name>', views.author_blogs, name = 'author_blogs'),
]
