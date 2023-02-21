from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),

    path('add-contact/', views.AddContact, name='add-contact'),
    path('profile/<int:pk>', views.ContactProfile, name='profile'),
    path('edit-contact/<int:pk>', views.EditContact, name='edit-contact'),
    path('delete-contact/<int:pk>', views.DeleteContact, name='delete-contact'),
]

