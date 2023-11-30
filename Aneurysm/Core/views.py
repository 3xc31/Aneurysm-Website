from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Core/index.html')

    request.user_agent.is_mobile # returns True
    request.user_agent.is_pc # returns False