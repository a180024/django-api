from django.urls import path, include
from . import views

app_name = 'files'

urlpatterns = [
    path('files/', views.FileListView.as_view(), name='file-list'),
    path('files/upload/', views.FileUploadView.as_view(), name='file-upload'),
    path('files/<int:pk>/', views.FileDetailView.as_view(), name='file-detail'),
    path('files/<int:pk>/update/', views.FileUpdateView.as_view(), name='file-update'),
    path('files/<int:pk>/delete/', views.FileDeleteView.as_view(), name='file-delete'),
]
