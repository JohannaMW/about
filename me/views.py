from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.mail import send_mail

from .forms import ContactForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            subject = "Message from {}".format(name)

            recipients = ['johanna.weinsziehr@gmail.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render_to_response("index.html", {
        'form': form,
    })
