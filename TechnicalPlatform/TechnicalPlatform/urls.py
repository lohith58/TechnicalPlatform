from django.contrib import admin
from django.urls import path,include
from taskmate import views as taskmate_views
from blog import views as blog_views
from users_app import views as users_app_views


urlpatterns = [


    path('admin/', admin.site.urls),
    path('schedule/',include('taskmate.urls')),
    path('account/',include('users_app.urls')),
    path('blog/',include('blog.urls')),
    path('contact',taskmate_views.contact,name='contact'),
    path('theory',users_app_views.theoryhome,name='theoryhome'),
    path('<str:type>/<int:value>',users_app_views.theory,name='theory'),
    path('RefundPolicy',taskmate_views.refund,name='refund'),
    path('TermsOfUse',taskmate_views.terms,name='terms'),
    path('PrivacyPolicy',taskmate_views.privacy,name='privacy'),
    path('FAQS',taskmate_views.faqs,name='faqs'),
    path('djangocheat',blog_views.djangocheatsheet,name='djangocheat'),
    path('pythoncheat',blog_views.pythoncheatsheet,name='pythoncheat'),
    path('javacheat',blog_views.javacheatsheet,name='javacheat'),
    path('springcheat',blog_views.springcheatsheet,name='springcheat'),
    path('hibernatecheat',blog_views.hibernatecheatsheet,name='hibernatecheat'),
    path('',taskmate_views.index,name='index'),
    path('<int:id>/share/',blog_views.mail_send_view),


]
