from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from platzigram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', local_views.hello),
    path('sorted_nums/', local_views.sorted_nums),
    path('hi/<str:name>/<int:age>/', local_views.hi),

    path('posts/', posts_views.list_posts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
