import matplotlib.pyplot as plt
import numpy


def F(**kwargs):
  locals().update(kwargs)
  return x * (1-x) * ((C2-C1) + (-A+b-C2)*y)


def G(**kwargs):
  locals().update(kwargs)
  return y * (1-y) * ((p1-p2+a) + (A+T)*x)


def E11(**kwargs):
  locals().update(kwargs)
  return y * (-A+b-C1) + (1-y)*(-C1)


def E12(**kwargs):
  locals().update(kwargs)
  return (1-y)*(-C2)


def E1(**kwargs):
  locals().update(kwargs)
  e11 = E11(**kwargs)
  e12 = E12(**kwargs)
  return x*e11 + (1-x)*e12


def E21(**kwargs):
  locals().update(kwargs)
  return x * (p1+A+a) + (1-x)*(p1+a)


def E22(**kwargs):
  locals().update(kwargs)
  return x*(p1-T)+(1-x)*p2


def E2(**kwargs):
  locals().update(kwargs)
  e21 = E21(**kwargs)
  e22 = E22(**kwargs)
  return y*e21 + (1-y)*e22
