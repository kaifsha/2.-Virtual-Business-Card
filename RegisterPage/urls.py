from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from Register import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/register/')),  
    path('register/', views.Register_fun, name='Register_fun'),  
    path('registration-sucess/', views.Register_form_sucess, name='Registration_sucess'), 
    path('qr_code/<int:id>/', views.qr_code, name='qr_code'),
    path('registration-sucess/details/<int:id>/', views.details, name='details'),

      # URL pattern for registration success page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



