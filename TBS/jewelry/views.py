
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login , logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator

from jewelry.models import Merchandise



# Create your views here.

class JewelryListView(View):
	def get(self,request):
		merchandises = Merchandise.objects.all()
		paginator = Paginator(merchandises, 100)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		return render(request,'merchandise_list.html',{'merchandises':page_obj})



