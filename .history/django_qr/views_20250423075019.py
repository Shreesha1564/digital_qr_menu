from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings


def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Generate QR Code
            qr = qrcode.make(url)
            print(qr)
    
    else:
        form = QRCodeForm()
        context = {
            'form': form,
        }
        return render(request, 'generate_qr_code.html', context)