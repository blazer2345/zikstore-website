from django.shortcuts import render

# Create your views here.

def productsPage(request):
  return render(request, 'productpage.html')