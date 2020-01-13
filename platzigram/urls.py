from django.contrib import admin
from django.urls import path

from platzigram import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('sorted_nums/', views.sorted_nums),
    path('hi/<str:name>/<int:age>/', views.hi)
]
