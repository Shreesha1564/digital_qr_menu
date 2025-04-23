from django.shortcuts import render 
from .forms import QRCodeForm
def generate_qr_code(request):
   form = QRCodeForm()
   context = {
                form': form
            }
   return render(request, 'qr_result.html', context)