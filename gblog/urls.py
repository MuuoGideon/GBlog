from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('login_user/', views.login_user, name='login-user'),
	path('logout_user/', views.logout_user, name='logout-user'),
	path('show_post/<post_id>/', views.show_post, name='show-post'),
	path('add_post/', views.add_post, name='add-post'),
	path('update_post/<post_id>/', views.update_post, name='update-post'),
	path('delete_post/<post_id>/', views.delete_post, name='delete-post'),
	path('search_post/', views.search_post, name='search-post'),
	path('dashboard/', views.dashboard, name='dash-board')
]