from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from Django_blog import settings
from posts.views import *

app_name = "posts"

urlpatterns = [
                  path('', BlogpostHome.as_view(), name='home'),
                  path('create/', BlogpostCreate.as_view(), name='create'),
                  path('edit/<str:slug>', login_required(BlogpostUpdate.as_view()), name='edit'),
                  path('<str:slug>/', BlogpostDetail.as_view(), name='detail'),
                  path('delete/<str:slug>/', BlogpostDelete.as_view(), name='delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
