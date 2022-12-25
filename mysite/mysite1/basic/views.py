from django.shortcuts import render
from .models import member
from .forms import MemberForm
from django.http import HttpResponseRedirect 
# Create your views here.

def index(request):
	obj = member.objects.get(id=1)
	context = {
	'object': obj
	}
	return render(request,'index.html',context)

def forms_create (request):
	form = MemberForm(request.POST or None )
	if form.is_valid():
		form.save()
	context = {
	'form': form
	}
	return render(request,'forms.html',context)	
