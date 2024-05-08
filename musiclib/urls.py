from django.urls import path
from config import settings
from musiclib.apps import MusiclibConfig
from musiclib.views import CustomLoginView, home, cutter_file, signup_without_confirmation, upload
from django.conf.urls.static import static


app_name = MusiclibConfig.name

urlpatterns = [
    path('', signup_without_confirmation, name='register'),
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('home/', home, name='home'),
    path('upload/', upload, name='upload'),
    path('cutter_file/<int:pk1>/<int:pk2>', cutter_file, name='cutter_file'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
