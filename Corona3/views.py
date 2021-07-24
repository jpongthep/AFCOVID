from django.shortcuts import render

from .forms import Corona3BasicDataForm


def Corona3BasicForm(request):
    

    form = Corona3BasicDataForm()
    context = {'form' : form}  


    return render(request, "Corona3/basicData.html",context)


