from django.urls import path
from . import views

# Add this import at the top
from django.contrib.auth.views import LoginView

# Update the urlpatterns list
urlpatterns = [
    path('', views.home, name='home'),
    path('platform/', views.platform, name='platform'),
    path('solutions/', views.solutions, name='solutions'),
    path('pricing/', views.pricing, name='pricing'),
    path('resources/', views.resources, name='resources'),
    path('company/', views.company, name='company'),
    # Update the login path to include 'accounts' prefix
    path('accounts/login/', LoginView.as_view(template_name='website/login.html'), name='login'),
    path('contact/', views.contact, name='contact'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('signup/', views.signup, name='signup'),  # Add this line
    path('security/', views.security, name='security'),
    path('compliance/', views.compliance, name='compliance'),
    path('addons/', views.addons, name='addons'),
    path('user-management/', views.user_management, name='user_management'),
    path('webappscanner/', views.webappscanner, name='webappscanner'),
    path('policy-generator/', views.policygenerator, name='policygenerator'),
    path('export-pdf/', views.export_pdf, name='export_pdf'),
    path('export-excel/', views.export_excel, name='export_excel'),
]