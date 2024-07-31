from django.http import HttpResponse

# Create your views here.
def clientes(request):
    return HttpResponse("Bienvenido a los clientes")