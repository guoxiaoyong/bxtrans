function F(x, y, C1, C2, A, T, a, b, p1, p2, dt):
  return x * (1-x) * ((C2-C1) + (-A+b-C2)*y)


function G(x, y, C1, C2, A, T, a, b, p1, p2, dt):
  return y * (1-y) * ((p1-p2+a) + (A+T)*x)


