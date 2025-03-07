from django.contrib import admin
from django.urls import path
from machine.views import CashMachineView, send_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cash_machine', CashMachineView.as_view(), name='items-endpoint'),
    path('media/<str:filename>', send_file, name='send_file')
]
