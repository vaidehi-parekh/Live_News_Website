from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="headlines"),
    path('all/',views.all,name="all"),
    path('technology/',views.technology,name="technology"),
    path('business/',views.business,name="business"),
    path('science/',views.science,name="science"),
    path('entertainment/',views.entertainment,name="entertainment"),
    path('sports/',views.sports,name="sports"),
]


