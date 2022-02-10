
from django.contrib import admin
from django.urls import path
from app.views import(
    index, 
    delete,
    add_post,
)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('delete/<str:id_>', delete),
    path('add_post/', add_post)
]
