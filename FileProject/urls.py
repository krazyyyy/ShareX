from django.urls import path
# from django_encrypted_filefield.constants import FETCH_URL_NAME
from django.conf.urls import url

from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload', views.upload_file, name="upload"),
    path('register', views.register_view, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('main', views.main_app, name='main'),
    path('download/<str:pk>', views.download_page, name="download"),
    path('delete/<str:pk>', views.delete_file, name="delete"),
    path('dec/<str:pk>', views.decrypt_func, name="dec"),
    path('enc/<str:pk>', views.encrypt_func, name="enc"),
]