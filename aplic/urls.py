from django.urls import path

from .views import IndexView, FuncionarioView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('funcionarios/', FuncionarioView.as_view(), name='funcionarios'),
]
