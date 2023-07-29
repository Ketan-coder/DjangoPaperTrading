from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('Accounts.urls')),
	path('', include('Transcation.urls')),
	path('', include('Stocks.urls')),
	path('', include('Options.urls')),
	path('', include('Portfolio.urls')),
	path('', include('Analysis.urls')),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
