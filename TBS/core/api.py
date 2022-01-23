# -*- coding: utf-8 -*-
from datetime import datetime

def combine_datetime_pk(pk,width = 12,datetime=datetime.now()):
	width-=6
	if(width<0):
		width=0
	return '{:%y%m%d}{:0{width}d}'.format(datetime,pk,width=width)
