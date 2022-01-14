from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from.forms import MovieRecordForm
from .models import MovieRecord

def homeView(request):
    template_name = 'App1/base.html'
    context = {}
    return render(request, template_name, context)

def addView(request):
    form=MovieRecordForm()
    if request.method == 'POST':
        form =MovieRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
            # return HttpResponse('order Placed')
    template_name = 'App1/Addmovie.html'
    context = {'form': form}
    return render(request, template_name, context)

def showMovieView(request):
    template_name = 'App1/ShowMovie.html'
    bk = MovieRecord.objects.all()
    context = {'bk': bk}
    return render(request, template_name, context)

def updateView(request,id_from_fe):
    vc = MovieRecord.objects.get(id=id_from_fe)
    form=MovieRecordForm(instance=vc)
    if request.method=='POST':
        form=MovieRecordForm(request.POST,instance=vc)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='App1/Addmovie.html'
    context={'form':form}
    return render(request,template_name,context)



def deleteView(request,id_from_fe):
    vc=MovieRecord.objects.get(id=id_from_fe)
    vc.delete()
    return redirect('show')

# Create your views here.

def search(request):
    if request.method=='POST':
        srch=request.POST.get('searchkey')
        st=MovieRecord.objects.all()
        # if srch not in st:
        #     return HttpResponse('record not found!!')
        record=MovieRecord.objects.filter(Movie_Name=srch)
        print(record)
        template_name='App1/searchMovie.html'
        context={'record':record}
        return render(request, template_name,context)

    template_name='App1/search.html'
    context={}
    return render(request, template_name, context)
