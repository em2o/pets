from django.shortcuts import render, redirect
from cachorro.forms import CachorroForm

# Create your views here.


def cadastro(request):
    form = CachorroForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args['msg'] = 'Cadastro Realizado com sucesso'
    
    
        return redirect('/')
    return render(request, 'cadastro_cachorro.html', args)