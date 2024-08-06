import quaternions.quaternion
#from dual_numbers import *
from src.dual_numbers import *
import math as m

qt=quaternions.quaternion.Quaternion

def qtexp(q):
	if type(q) in [type(1),type(1.0)]:
		return qt(m.exp(q),0,0,0)
	v=qt(0,q.x,q.y,q.z)
	norm=v.norm()
	v_u=v.unit()
	real=m.cos(norm)
	return (v_u*m.sin(norm)+qt(real,0,0,0))*m.exp(q.w)

def qtlog(q):
	v=qt(0,q.x,q.y,q.z)
	v_u=v.unit()
	return v_u*m.acos(q.w/q.norm())+qt(m.log(q.norm),0,0,0)


