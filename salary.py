from enum import Enum

#底薪
base = 2320

#岗位
class Position(Enum):
	master = 1
	internet = 2

#提成
commision = {
	(4,4.5):0.03,
	(3.5,4):0.02,
	(3,3.5):0.015,
	(2.85,3):0.01,
	(2.7,2.85):0.0075,
	(2.55,2.7):0.005,
	(2.35,2.55):0.0025,
	(0,2.35):0
}

#奖励
extra_bonus = 1000

#津贴
allowance_seniority_base = 100
allowance_travel_daily = 10
allowance_position = {
	Position.master:500,
	Position.internet:2000,
}

#保险
insurance = 1100

#奖励
benefit = 0