from django.shortcuts import render
def show_main(request):
    context = {
        'app name' : 'Af Classico',
        'name': 'M. Adella Fathir Supriadi',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
# Create your views here.
