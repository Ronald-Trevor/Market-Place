from django.urls import path
from .views import detail

app_name = 'item'

urlpatterns = [
    path('<int:primary_key>',detail,name='detail')
]
