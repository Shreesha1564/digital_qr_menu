from django.shrotcuts import render 
def generate_qr_code(request):
   return render(request,'generate_qr_code.html')