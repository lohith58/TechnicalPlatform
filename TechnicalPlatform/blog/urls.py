from django.urls import path
from blog import views

urlpatterns = [

    path("",views.post_list_view,name='blog'),
    path('tag/?<slug:tag_slug>/',views.post_list_view,name='post_list_by_tag_name'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail_view,name='post_detail'),


]
