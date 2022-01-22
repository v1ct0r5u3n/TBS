from django import forms
from .models import Person,Employee,Customer

class EmployeeLoginForm(forms.Form):
	mobile = forms.CharField(
			label='手机号',
			required=True,
			max_length = 20,
			widget = forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'请输入手机号'
				}
			),
			error_messages={
				'required':'手机号不能为空',
				'max_length':'长度不能超过20',
			}
		)
	password = forms.CharField(
			label = '密码',
			required = True,
			min_length = 3,
			max_length = 50,
			widget = forms.PasswordInput(
				attrs = {
					'class':'form-control',
					'placeholder':'请输入密码',
				}
			),
			error_messages = {
				'required':'密码不能为空',
				'min_length':'密码长度不能少于6个字符',
				'max_length':'密码长度不能多于50个字符'
			}
		)

	def clean_mobile(self):
		mobile = self.cleaned_data['mobile']
		try:
			Employee.objects.get(mobile=mobile)
			print(mobile)
		except:
			raise forms.ValidationError('手机号不存在','invalid')
		else:
			return mobile
