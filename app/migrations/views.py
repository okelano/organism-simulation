from django.shortcuts import render

# Example view
def index(request):
    return render(request, 'index.html')
