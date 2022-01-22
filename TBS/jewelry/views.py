
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login , logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect

from jewelry.models import Merchandise



# Create your views here.

class JewelryListView(View):
	def get(self,request):
		merchandises = Merchandise.objects.all()[:20]

		return render(request,'merchandise_list.html',{'merchandises':merchandises})



