import collections

from recordclass import recordclass

from gbm import RandomProcess, get_series


def which_case(x=0,y=0,C1=0,C2=0,A=0,T=0,a=0,b=0,p1=0,p2=0,dt=0, **kwargs):
  #print = lambda x:None
  if p1 + a + A < p2 - T:
    print('compare C1 and C2: %s, %s' % (C1, C2))
  else:
    print('compare b and A+C1: %s, %s' % (b, A+C1))


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
  StateType = recordclass('Evo_state', ['x', 'y', 't'])

  def __next__(self):
    res = self.StateType(**self.state._asdict())
    param = {**self.param._asdict(), **self.state._asdict()}
    dx = F(**param) * self.param.dt
    dy = G(**param) * self.param.dt

    self.state.x += dx
    self.state.y += dy
    self.state.t += self.param.dt
    return res


def get_sim_results(C2, b, A, N=30, dt=0.1):
  state = {'x': 0.5, 'y': 0.5}
  evo = Evo.create(
      C1=2,
      C2=C2,
      A=A,
      T=1.1,
      a=0.9,
      b=b,
      p1=0.8,
      p2=4,
      dt=dt,
      t=0,
      **state,
  )

  res = []
  for _ in range(N+1):
    r = next(evo)
    res.append(dict(r._asdict()))
  return res
