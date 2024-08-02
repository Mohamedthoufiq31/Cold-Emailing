from django.shortcuts import render
from .forms import EmailForm

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # Process the form data and send an email
            # ...
            return render(request, 'send_email.html', {'form': form})
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})
