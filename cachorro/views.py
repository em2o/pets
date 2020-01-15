from django.shortcuts import render, redirect
from cachorro.forms import CachorroForm 
from cachorro.models import Cachorro

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


def detail(request,id):
    cachorro = cachorro.objects.get(id=id)
    args = {
        'cachorro':cachorro,
    }
    return render(request, 'detail_cachorro.html', args)

def delete(request, id ):
    cachorro =cachorro.objects.get(id=id)

    args = {
        'cachorro':cachorro
    }

    cachorro.delete()
    return render (request, 'delete_cachorro.html',)

def update(request, id):
    cachorro = Cachorro.objects.get(id=id)
    form = CachorroForm(request.POST or None, instance=cachorro)

    if form.is_valid():
        form.save()
        return redirect(f'../detail/{cachorro.id}')

    args = {
        'cachorro':cachorro,
        'form':form
    }
    
    return render(request,'update_cachorro.html', args)  
    


