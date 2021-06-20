from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list_view, name = "home-view"),
    path('post/<int:pk>', views.StoryDetailView.as_view(), name= 'post-detail'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
