from django.shortcuts import render 
from .forms import QRCodeForm
def generate_qr_code(request):
   form = QRCodeForm(request.POST)
   return render(request,'generate_qr_code.html')