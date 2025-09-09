from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2406495640',
        'name': 'M. Adella Fathir Supriadi',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
# Create your views here.
