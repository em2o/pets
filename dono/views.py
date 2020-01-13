from django.shortcuts import render, redirect
from dono.forms import DonoForm

# Create your views here.


def cadastro(request):
    form = DonoForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args['msg'] = 'Cadastro Realizado com sucesso'
        return redirect('/')
    return render(request, 'cadastro.html', args)

def detail(request,id):
    donos = Dono.objects.get(id=id)
    args = {
        'donos':donos,
    }
    return render(request, 'detail_dono.html', args)

def delete(request, id ):
    dono = Dono.objects.get(id=id)

    args = {
        'donos':dono
    }

    dono.delete()
    return render (request, 'delete_dono.html',)

def update(request, id):
    dono = Dono.objects.get(id=id)
    form=DonoForm(request.POST or None, instance=dono)

    if form.is_valid():
        form.save()
        return redirect(f'../detail/{dono.id}')

        args = {
            'dono':dono,
            'form':form
        }
    return render(request,'update_dono.html')  
    


