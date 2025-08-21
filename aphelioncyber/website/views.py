from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import UserSubscription
from django.http import HttpResponse
import csv
from reportlab.pdfgen import canvas
from io import BytesIO

def home(request):
    return render(request, 'website/home.html')

def platform(request):
    return render(request, 'website/platform.html')

def solutions(request):
    return render(request, 'website/solutions.html')

def pricing(request):
    return render(request, 'website/pricing.html')

def resources(request):
    return render(request, 'website/resources.html')

def company(request):
    return render(request, 'website/company.html')

# Remove or comment out the existing login view
# def login(request):
#     return render(request, 'website/login.html')

# Add these imports at the top
from django.contrib.auth.views import LoginView

# Add the custom login view
class CustomLoginView(LoginView):
    template_name = 'website/login.html'
    redirect_authenticated_user = True

def forgot_password(request):
    if request.method == 'POST':
        # Add your password reset logic here
        # For example, send a reset email
        messages.success(request, 'Password reset instructions have been sent to your email.')
        return redirect('login')
    return render(request, 'website/forgot_password.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. We will get back to you soon!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'website/contact.html', {'form': form})

def signup(request):
    return render(request, 'website/signup.html')

def security(request):
    return render(request, 'website/security.html')

def compliance(request):
    return render(request, 'website/compliance.html')

def addons(request):
    return render(request, 'website/addons.html')

def webappscanner(request):
    return render(request, 'website/webappscanner.html')

# @login_required
def user_management(request):
    users = User.objects.all()
    return render(request, 'website/user_management.html', {'users': users})
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            username = request.POST.get('email')
            email = request.POST.get('email')
            name = request.POST.get('name')
            subscription_type = request.POST.get('subscription_type')
            
            # Create user
            user = User.objects.create_user(username=username, email=email)
            if ' ' in name:
                first_name, last_name = name.rsplit(' ', 1)
                user.first_name = first_name
                user.last_name = last_name
            else:
                user.first_name = name
            user.save()
            
            # Create subscription
            UserSubscription.objects.create(
                user=user,
                subscription_type=subscription_type,
                status='active'
            )
            messages.success(request, 'User added successfully')
            return redirect('user_management')
            
        elif action == 'delete':
            user_id = request.POST.get('user_id')
            User.objects.filter(id=user_id).delete()
            messages.success(request, 'User deleted successfully')
            return redirect('user_management')
            
    users = User.objects.select_related('usersubscription').all()
    return render(request, 'website/user_management.html', {'users': users})

def policygenerator(request):
    return render(request, 'website/policygenerator.html')


def export_pdf(request):
    # Create a file-like buffer to receive PDF data
    buffer = BytesIO()
    
    # Create the PDF object, using the buffer as its "file"
    p = canvas.Canvas(buffer)
    
    # Draw things on the PDF
    p.drawString(100, 800, "Asset Inventory Report")
    y = 750
    # Add headers
    p.drawString(100, y, "Asset Name")
    p.drawString(250, y, "Description")
    p.drawString(400, y, "Status")
    y -= 20
    
    # Add sample data (replace with your actual data)
    sample_data = [
        ["AMZN-EC2-Linux-App", "Server that is installed in project", "Running"],
        # Add more rows as needed
    ]
    
    for row in sample_data:
        p.drawString(100, y, row[0])
        p.drawString(250, y, row[1])
        p.drawString(400, y, row[2])
        y -= 20
    
    # Close the PDF object cleanly
    p.showPage()
    p.save()
    
    # Get the value of the BytesIO buffer and return it
    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="asset_inventory.pdf"'
    response.write(pdf)
    return response

def export_excel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="asset_inventory.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Asset Name', 'Description', 'Status'])
    
    # Add sample data (replace with your actual data)
    sample_data = [
        ['AMZN-EC2-Linux-App', 'Server that is installed in project', 'Running'],
        # Add more rows as needed
    ]
    
    for row in sample_data:
        writer.writerow(row)
    
    return response