from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import RequestModel, Song, Rajesh, Bhuvana
from .form import RequestForm
from django.urls import reverse_lazy
from django.views import View
# Create your views here.


def homepage(request):
    images = Song.objects.all()
    context = {'image': images}
    print(context)
    return render(request, 'home2.html', context)
    
class omePage(CreateView):
  model = RequestModel
  form_class = RequestForm
  template_name = 'home.html'
  success_url = reverse_lazy('home')
  
  
def HomePage(request):
  form = RequestForm()
  songs = Song.objects.all()
  rajesh = Rajesh.objects.all()
  bhuvana = Bhuvana.objects.all()
  
  if request.method == 'POST':
    print('post request triggered')
    form = RequestForm(request.POST)
    print('got form data')
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      form = RequestForm()
  context = {'form': form, 'songs': songs, 'rajesh': rajesh, 'bhuvana': bhuvana} 
  return render(request, 'home.html', context)
      
    