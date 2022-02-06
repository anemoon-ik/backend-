
from django.contrib import admin
from django.urls import path
from app.views import(
    index, 
    delete
)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('delete/<str:id_>', delete),

]
