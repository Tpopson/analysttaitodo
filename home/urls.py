from django.urls import path
from .views import index, deltodo, completed, uncompleted


urlpatterns = [
    path('', index, name='index'),
    path('completed', completed, name='completed'),
    path('uncompleted', uncompleted, name='uncompleted'),
    path('deltodo', deltodo, name='deltodo'),
]
