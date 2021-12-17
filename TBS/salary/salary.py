#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division
from enum import Enum


#底薪
_base = 2120

#岗位
class Position(Enum):
	master = 1
	internet = 2

class ItemCatgory(Enum):
	end_product = 1 #成品
	pearl = 2 #裸珠
	pedestal = 3 #空托
	special_price = 4 #特价
	accessory = 5 #配件
	online_price = 6 #线上实价


#提成
_commisions = {}
_commisions["成品"] = {
	(4,10):3,
	(3.5,4):2,
	(3,3.5):1.5,
	(2.85,3):1,
	(2.7,2.85):0.75,
	(2.55,2.7):0.5,
	(2.35,2.55):0.25,
	(0,2.35):0
}
_commisions["裸珠"] = _commisions["成品"]
_commisions["空托"] = {
	(5,10):1,
	(4.75,5):0.75,
	(4.5,4.75):0.5,
	(4.25,4.5):0.35,
	(4,4.25):0.25,
	(0,4):0
}
_commisions["特价"] = {
	(10,10):1,
	(9,10):0.75,
	(8,9):0.5,
	(7,8):0.25,
	(0,7):0
}

_commisions["配件"] = _commisions["特价"]
_commisions["线上实价"] = {
	(10,10):2,
	(9.5,10):1.5,
	(9,9.5):1,
	(8.5,9):0.75,
	(8,8.5):0.5,
	(7,8):0.25,
	(0,7):0
}

#奖励
_extra_bonus = 1000

#津贴
_allowance_seniority_base = 100
_allowance_travel_daily = 10
_allowance_position = {
	Position.master:500,
	Position.internet:2000,
}

#保险
_insurance = 1100

#奖励
_benefit = 1000

#个人任务
_personal_goal = 100

#店任务
_shop_goal = 100


def calc_item_commision(price_catgory, tag_price, sale_price):
	'''
	计算商品提成.
	'''
	discount = sale_price/tag_price*10
	for l,r in _commisions[price_catgory]:
		if (discount>=l and discount<r) or (discount==l and l==r):
			return round(sale_price*_commisions[price_catgory][(l,r)]/100.0,2)
	return 0

def calc_commisions():
	'''
	计算提成.
	个人提成+个人超额提成+集体提成+店超额提成+店长提成
	'''
	pass

def calc_allowance(position,duty_days,years_of_service):
	'''
	计算津贴.
	工龄+车补+岗位津贴
	'''
	return years_of_service*_allowance_seniority_base+\
	duty_days*_allowance_travel_daily+\
	_allowance_position.get(position,0)


def calc_salary(commisions,have_insurance,allowance,benefit=_benefit):
	'''
	计算月工资.
	基本工资+提成+保险+津贴+奖励
	'''
	insurance = 0
	if not have_insurance:
		insurance = _insurance;
	return _base+commisions+insurance+allowance+benefit

if __name__ == "__main__":
	print("test")
	print(calc_item_commision("裸珠",100,90)==2.7 and
		calc_item_commision("裸珠",100,45)==1.35 and
		calc_item_commision("裸珠",100,43)==1.29 and
		calc_item_commision("裸珠",100,40)==1.2 and
		calc_item_commision("裸珠",100,37)==0.74 and
		calc_item_commision("裸珠",100,35)==0.7 and
		calc_item_commision("裸珠",100,33)==0.49 and
		calc_item_commision("裸珠",100,30)==0.45 and
		calc_item_commision("裸珠",100,29)==0.29 and
		calc_item_commision("裸珠",100,28.5)==0.21 and
		calc_item_commision("裸珠",100,27.5)==0.21 and
		calc_item_commision("裸珠",100,26)==0.13 and
		calc_item_commision("裸珠",100,25)==0.06 and
		calc_item_commision("裸珠",100,24)==0.06 and
		calc_item_commision("裸珠",100,20)==0)

