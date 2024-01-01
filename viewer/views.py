# import viewer_process as process
from . import viewer_process as process
from django.shortcuts import render

# Create your views here.

def index(request):
    # context = {'dic_menu_item': process.create_menu_item()}
    dic_menu_item = process.create_menu_item()
    context = {}
    context['States'] = {
        'California': ['Los Angeles', 'San Diego'],
        'Florida': ['Miami', 'Orlando'],
        'Texas': ['Dallas', 'St. Antonio']
    }
    return render(request, "viewer/index.html", context)
