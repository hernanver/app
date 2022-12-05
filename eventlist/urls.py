from django.contrib import admin
from django.urls import path
from . import views as eventlist_views 
from django.conf.urls.static import static
from django.conf import settings
from .views import EventListView



urlpatterns = [
    path('', EventListView.as_view(), name="base"),
    path('admin/', admin.site.urls, name="admininstrador"),
    path('<int:event_id>',eventlist_views.detail, name="detail")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)