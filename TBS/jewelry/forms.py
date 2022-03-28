# -*- coding: utf-8 -*-
from django.forms import ModelForm

from .models import Record,MerchandiseRecord,RecordPay


class RecordPayForm(ModelForm):
	class Meta:
		model = RecordPay
		exclude = ()

class MerchandiseRecordForm(ModelForm):
	class Meta:
		model = MerchandiseRecord
		exclude = ()