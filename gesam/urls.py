from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

import myapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name='home'),
    path('home/', myapp.views.index, name='home'),
    path('contact/', myapp.views.contact, name='contact'),
    path('beliefs/', myapp.views.beliefs, name='beliefs'),
    path('sermons/', myapp.views.sermons, name='sermons'),
    url(r'^home', myapp.views.index, name='home'),
    url(r'^contact', myapp.views.contact, name='contact'),
    url(r'^beliefs', myapp.views.beliefs, name='beliefs'),
    url(r'^sermons', myapp.views.sermons, name='sermons'),
    url(r'^donations', myapp.views.donations, name='donations'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






