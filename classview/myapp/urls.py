from django.urls import path, include

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.NoteList.as_view(), name='index'),
    path('create/', views.NoteCreate.as_view(), name='create'),
    path('delete/<int:pk>/', views.NoteDelete.as_view(), name='delete'),
    path('update/<int:pk>/', views.NoteUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.NoteDetail.as_view(), name='detail'),
]
