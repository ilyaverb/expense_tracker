from django.contrib import admin
from django.urls import path, include

from config.yasg import urlpatterns as docs_urls

urlpatterns = [
    path(
        'admin/', admin.site.urls
    ),
    path(
        'api/',
        include(
            ('expense_tracker.authentication.urls', 'auth'),
            namespace='auth')
    ),
    path(
        'api/',
        include(('expense_tracker.core.urls', 'core'), namespace='core')
    ),
]

urlpatterns += docs_urls
