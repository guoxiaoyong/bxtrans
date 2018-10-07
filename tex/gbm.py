import math
import itertools
import collections
import numpy as np
import matplotlib.pyplot as plt

from recordclass import recordclass


def get_series(iterator, num):
  s = []
  t = []
  for state in itertools.islice(iterator, 0, num, 1):
    s.append(state.s)
    t.append(state.t)
  return s, t


class RandomProcess(object):
  ParamType = None
  StateType = recordclass('Simple_state', ['s', 't'])

  def __init__(self, param, state):
    self._param = param
    self._state = state

  def __iter__(self):
    return type(self)(self.param, self.state)

  @classmethod
  def create(cls, **kwargs):
    param_kwargs = {key: value for key, value in kwargs.items() if key in cls.ParamType._fields}
    state_kwargs = {key: value for key, value in kwargs.items() if key in cls.StateType._fields}
    return cls(cls.ParamType(**param_kwargs), cls.StateType(**state_kwargs))

  @property
  def param(self):
    return self._param

  @property
  def state(self):
    return self._state


class GBMotion(RandomProcess):
  ParamType = collections.namedtuple(
      'GBMotion_param', ['mu', 'sigma', 'dt'])

  def __next__(self):
    dw = np.random.normal(loc=0.0, scale=math.sqrt(self.param.dt))
    ds = self.param.mu * self.state.s * self.param.dt + self.param.sigma * self.state.s * dw
    self.state.s += ds
    self.state.t += self.param.dt
    return self.state


# dxt=θ(μ−xt)dt+σdWt
class OUProcess(RandomProcess):
  ParamType = collections.namedtuple(
      'OUProcess_param',
      ['theta', 'mu', 'sigma', 'dt'])

  def __next__(self):
    dw = np.random.normal(loc=0.0, scale=math.sqrt(self.param.dt))
    ds = self.param.theta*(self.param.mu - self.state.s)*self.param.dt + self.param.sigma * dw
    self.state.s += ds
    self.state.t += self.param.dt
    return self.state


if __name__ == '__main__':
  x = GBMotion.create(mu=0.000002, sigma=0.02, dt=0.1, s=0.1, t=0)
  x = OUProcess.create(theta=0.2, mu=0.02, sigma=0.1, dt=0.1, s=0, t=0)
  s, t = get_series(x, 100)

  plt.figure()
  plt.plot(t, s, marker='.')
  plt.show()
