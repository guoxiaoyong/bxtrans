import collections

import matplotlib.pyplot as plt
import numpy

from gbm import RandomProcess, get_series


def F(x=0,y=0,C1=0,C2=0,A=0,T=0,a=0,b=0,p1=0,p2=0,dt=0, **kwargs):
  return x * (1-x) * ((C2-C1) + (-A+b-C2)*y)


def G(x=0,y=0,C1=0,C2=0,A=0,T=0,a=0,b=0,p1=0,p2=0,dt=0, **kwargs):
  return y * (1-y) * ((p1-p2+a) + (A+T)*x)


def E11(x=0,y=0,C1=0,C2=0,A=0,T=0,a=0,b=0,p1=0,p2=0,dt=0, **kwargs):
  return y * (-A+b-C1) + (1-y)*(-C1)


def E12(x=0,y=0,C1=0,C2=0,A=0,T=0,a=0,b=0,p1=0,p2=0,dt=0, **kwargs):
  return (1-y)*(-C2)


def E1(x=0,y=0,C1=0,C2=0,A=0,T=0,a=0,b=0,p1=0,p2=0,dt=0, **kwargs):
  e11 = E11(**locals())
  e12 = E12(**locals())
  return x*e11 + (1-x)*e12


def E21(x=0,y=0,C1=0,C2=0,A=0,T=0,a=0,b=0,p1=0,p2=0,dt=0, **kwargs):
  return x * (p1+A+a) + (1-x)*(p1+a)


def E22(x=0,y=0,C1=0,C2=0,A=0,T=0,a=0,b=0,p1=0,p2=0,dt=0, **kwargs):
  return x*(p1-T)+(1-x)*p2


def E2(x=0,y=0,C1=0,C2=0,A=0,T=0,a=0,b=0,p1=0,p2=0,dt=0, **kwargs):
  e21 = E21(**locals())
  e22 = E22(**locals())
  return y*e21 + (1-y)*e22


class Evo(RandomProcess):
  ParamType = collections.namedtuple(
      'EvoProcess_param',
      ['C1', 'C2', 'A', 'T', 'a', 'b', 'p1', 'p2', 'dt'])

  def __next__(self):
    param = {**self.param._asdict(), **self.state._asdict(), **self.state.s}
    dx = F(**param) * self.param.dt
    dy = G(**param) * self.param.dt

    self.state.s['x'] += dx
    self.state.s['y'] += dy
    self.state.t += self.param.dt
    return self.state


state = {'x': 0.1, 'y': 0.1}
xx = Evo.create(
    C1=2,
    C2=1.8,
    A=0.5,
    T=1.1,
    a=0.9,
    b=4.7,
    p1=1.8,
    p2=4,
    dt=0.1,
    s=state,
    t=0,
)

#s, t = get_series(xx, 10)
#for n in s: print(n)
for n in range(100000):
  print(next(xx))

#plt.figure()
#plt.plot(t, s, marker='.')
#plt.show()
