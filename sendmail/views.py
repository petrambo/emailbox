from django.shortcuts import render
from mailapp.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
# Create your views here.
#DataFlair #Send Email
def sendmail(request):
    sub = forms.Contactemail()
    if request.method == 'POST':
        sub = forms.Contactemail(request.POST)
        subject = str(sub['subject'].value())
        message = str(sub['message'].value())
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'sendmail/success.html', {'recepient': recepient})
    return render(request, 'sendmail/index.html', {'form':sub})