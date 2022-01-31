from django.urls import path 
from . import views
urlpatterns = [
    path('security-question-list/', views.SecurityQuestionsAll,name='security-question-list'),
    path('register/', views.register,name='register'),
    path('verify-pin/', views.verifyPin,name='verify-pin'), 
    path('save-password/', views.savePassword,name='save-password'), 
    path('change-password/', views.changePassword,name='change-password'), 
    path('forgot-password/', views.forgotPassword,name='forgot-password'), 
    path('reset-password/', views.resetPassword,name='reset-password'), 
    path('add-device/', views.addDevice,name='add-device'), 
]
