from django.contrib import admin
from django.urls import path,include

import blog.views
from blog import views
from django.urls import path,include
#from .views import indexViews







urlpatterns = [
    path("hello",views.hello),
    path('content',blog.views.article_content),
    path('index',blog.views.get_index_page),
    #path('detail',blog.views.get_detail_page),
    path('detail/<int:article_id>',blog.views.get_detail_page),

]