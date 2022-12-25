from django import forms
from .models import member

class MemberForm(forms.ModelForm):
	class Meta:
		model = member
		fields = [
'name',
'last_name',
'email',

		]