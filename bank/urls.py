from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('viewallcust',views.viewallcust,name='viewallcust'),
    path('transfer',views.transfer,name='transfer'),
    path('history',views.history,name='history'),
    path('makechange',views.makechange,name='makechange')
]