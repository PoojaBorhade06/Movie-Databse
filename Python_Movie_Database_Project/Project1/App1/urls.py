from .import views
from django.urls import path
urlpatterns=[
    path('h/',views.homeView,name='home'),
    path('b/', views.addView, name='book'),
    path('s/', views.showMovieView, name='show'),
    path('search/', views.search, name='search'),
    path('u<int:id_from_fe>/',views.updateView,name='update'),
    path('d<int:id_from_fe>/',views.deleteView,name='delete')

]