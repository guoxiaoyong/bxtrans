function F(x, y, C1, C2, A, T, a, b, p1, p2, dt):
  return x * (1-x) * ((C2-C1) + (-A+b-C2)*y)


function G(x, y, C1, C2, A, T, a, b, p1, p2, dt):
  return y * (1-y) * ((p1-p2+a) + (A+T)*x)


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


def get_sim_results(**kwargs):
  x = kwargs.get('x', 0.5)
  y = kwargs.get('y', 0.5)
  evo = Evo.create(**kwargs)

  res = []
  N = kwargs.get('N', 40)
  for _ in range(N+1):
    r = next(evo)
    res.append(dict(r._asdict()))
  return res


