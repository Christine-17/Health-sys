from django.shortcuts import render,redirect
from .models import Inquiry
from django.core.mail import send_mail  # If you want to send emails
from django.http import HttpResponse

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        # Basic rule-based chatbot logic
        if 'fever' in user_input.lower():
            bot_response = 'It sounds like you might have a fever. Please stay hydrated and consult a doctor if symptoms persist.'
        elif 'headache' in user_input.lower():
            bot_response = 'Headaches can be caused by various factors. Try resting, staying hydrated, and consulting a doctor if it persists.'
        else:
            bot_response = 'I am not sure about that. Please consult a healthcare professional.'

        # Save conversation to database
        inquiry = Inquiry(user_input=user_input, bot_response=bot_response)
        inquiry.save()

        return render(request, 'chatbot/chat.html', {'user_input': user_input, 'bot_response': bot_response})
    
    return render(request, 'chatbot/chat.html')
def about_view(request):
    return render(request, 'chatbot/about.html')
def home_view(request):
    return render(request, 'chatbot/dashboard.html') 
def online_shopping_view(request):
    return render(request, 'chatbot/online_shopping.html') 

def contact_view(request):
    return render(request, 'chatbot/contact.html') 
def online_counselling(request):
    return render(request, 'chatbot/online_counselling.html')
def cart_view(request):
    return render(request, 'chatbot/cart.html')
def upload_prescription_view(request):
    # Add logic for handling prescription upload (e.g., form submission)
    return render(request, 'chatbot/upload_prescription.html')
def schedule_counselling_view(request):
    # Your logic here...
    return render(request, 'chatbot/schedule_counselling.html')


def contact_form_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Optional: Send an email or process the form data as needed
        send_mail(
            f'Contact form submission from {name}',
            message,
            email,
            ['recipient@example.com'],  # Replace with your recipient email
        )

        # Redirect to a success page or render a success message
        return redirect('contact_success')  # Adjust as necessary

    return HttpResponse('Invalid request method.', status=405)

def contact_success(request):
    return render(request, 'chatbot/contact_success.html')  # Create this template

from .forms import ImageUploadForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Replace with your success URL
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})