from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path
from Django_blog import settings
from posts.views import *

app_name = "posts"
"""Cette variable est utile lorsque nous voulons
 rediriger vers une url de cette app , mais à la place nous pouvons aussi mettre un param
 namespace
dans notre fonction include """

urlpatterns = [
                  path('', BlogpostHome.as_view(), name='home'),
                  path('create/', BlogpostCreate.as_view(), name='create'),
                  path('edit/<str:slug>', login_required(BlogpostUpdate.as_view()), name='edit'),
                  path('<str:slug>/', BlogpostDetail.as_view(), name='detail'),
                  path('delete/<str:slug>/', BlogpostDelete.as_view(), name='delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""L'ajout des fichiers static passe par cette dernierre ligne avec un "+" et la fonction static() """
