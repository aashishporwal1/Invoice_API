"""
URL configuration for invoice_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from invoices.views import InvoiceListCreateView, InvoiceDetailView, InvoiceDetailListCreateView, InvoiceDetailDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('api/invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('api/invoice_details/', InvoiceDetailListCreateView.as_view(), name='invoice-detail-list-create'),
    path('api/invoice_details/<int:pk>/', InvoiceDetailDetailView.as_view(), name='invoice-detail-detail'),
]
