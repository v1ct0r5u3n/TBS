
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login , logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect

from .login_forms import EmployeeLoginForm

# Create your views here.

class EmployeeLoginView(View):
	def get(self,request):
		return render(request,'login.html',{'form':EmployeeLoginForm()})

	def post(self,request):
		form = EmployeeLoginForm(request.POST)
		if(form.is_valid()):
			mobile = request.POST['mobile']
			password = request.POST['password']
			employee = authenticate(request,username=mobile,password=password)
			if employee is not None:
				login(request,employee)
				request.session['uid'] = employee.id
				request.session['mobile'] = employee.mobile
				if employee.name:
					request.session['name'] = employee.name
				else:
					request.session['name'] = employee.mobile
				
				return HttpResponseRedirect('/')
			else:
				messages.add_message(request,messages.ERROR,'手机号和密码不匹配')

		return render(request,'login.html',{'form':form})

class EmployeeIndexView(View):
	def get(self,request):
		return render(request,'base.html',{})