# -*- coding: utf-8 -*-
from django.db import models
from jewelry.models import Depot,Record


#借货单
class B2BRecord(Record):
	depot = models.ForeignKey(Depot,on_delete=models.CASCADE)

class B2BConfirm(B2BRecord):
	record = models.OneToOneField(B2BRecord,on_delete=models.CASCADE,related_name='confirm')
