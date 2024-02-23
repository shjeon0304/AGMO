from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('new/', views.new, name = 'new'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('index/', views.index, name='index'), 
    
    path('calender/', views.calender, name= 'calender'),
    path('growth/', views.growth, name= 'growth'),
    path('diary/', views.diary, name='diary'),
    path('create_diary/',views.page_create, name='create_diary'),
    path('login/',views.login,name='login'),

]
