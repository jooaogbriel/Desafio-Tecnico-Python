from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .functions import get_stores_from_database, refresh_database


def datas(request):
    
    data_list = get_stores_from_database()

    return render(request, 'transactions.html', {'data_list': data_list})


def arquivo(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            refresh_database(request.FILES['file'])

            return redirect('datas')
            
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
