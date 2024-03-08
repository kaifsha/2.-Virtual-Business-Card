

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Register


def Register_fun(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            register = form.save()
            # Generate QR code for the registered user
            register.generate_qr_code()
            return redirect('Registration_sucess')
    else:
        form = RegisterForm()
    return render(request, 'Register/register.html', {'form': form})

def Register_form_sucess(request):
    registers = Register.objects.all()
    return render(request, 'Register/Registration_sucess.html', {'registers': registers})

# def details(request, id):
#     register = Register.objects.get(id=id)
#     return render(request, 'RegisterApp/details.html', {'register': register})

def qr_code(request, id):
    register = Register.objects.get(id=id)
    qr_image = register.qr_code
    return HttpResponse(qr_image.read(), content_type="image/png")




def details(request, id):
    registers = Register.objects.get(id=id)
    return render(request, 'Register/card.html', {'registers': registers})
