from django.urls import path
from .import views


app_name='reviewapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('reviews/<int:nu>/',views.vreview,name='reviews'),
    path('new/',views.new,name='new'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]