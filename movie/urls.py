from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name = 'home'),
    path('detail/<int:id>',views.detail,name = 'detail'),
    path('category/<slug>/',views.category,name = 'category'),
    path('reg/',views.registration,name = 'reg'),
    path('logout/',views.log_out,name = 'logout'),
    path('login/',views.log_in,name = 'login')
]