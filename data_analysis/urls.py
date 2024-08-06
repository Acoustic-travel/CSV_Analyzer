from django.urls import path
from data_analysis import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results/<int:pk>/', views.results, name='results'),
]
from data_analysis.views import debug_view

urlpatterns = [
    # ... your other url patterns ...
    path('debug/', debug_view, name='debug'),
]