from django.shortcuts import render
from django.views import View
from .models import*

# Create your views here.

class HomeView(View):
    """Main View"""

    templates_name = 'index.html'

    invoices = Invoice.objects.all()
    
    context = {
        'invoices': invoices
    }

    def get(self, request, *args, **kwags):
        return render(request, self.templates_name, self.context)
    
    def post(self, request, *args, **kwags):
        return render(request, self.templates_name, self.context)