from django.shortcuts import render 
from .forms import QRCodeForm
def generate_qr_code(request):
   form = QRCodeForm(request.POST)
   context = {
                'res_name': res_name,
                'qr_url': qr_url,
                'file_name': file_name,
            }
            return render(request, 'qr_result.html', context)