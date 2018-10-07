import itertools
import matplotlib.pyplot as plt
import numpy as np

from common import get_sim_results

def main():
  C1 = 2
  markers = itertools.cycle('oDs*')
  c2_list = [1.7, 1.8, 2.1, 2.2]
  b = 4.7
  A = 0.5
  title = '$C_1$=2, $A$={A}, $T$=1.1, $a$=0.9, $b$={b}, $\pi_1$=0.8, $\pi_2$=4\n$\pi_1 + a + A < \pi_2 - T$'.format(A=A,b=b)
  plt.figure()
  for C2 in c2_list:
    res = get_sim_results(C2, b, A, dt=0.1, N=300)
    t = [v['t'] for v in res]
    x = [v['x'] for v in res]
    y = [v['y'] for v in res]
    #plt.plot(t, x, marker=next(markers), label='$C_2$=%s' % C2)
    plt.plot(t, y, marker=next(markers), label='$C_2$=%s' % C2)
  plt.title(title)
  plt.ylabel('$y$')
  plt.xlabel('Time($t$)')
  plt.legend(loc='center right')
  plt.grid()
  plt.xticks(np.arange(0, 31, step=2))
  plt.yticks(np.arange(0, 1.2, step=0.2))
  plt.ylim(0, .52)
  plt.xlim(left=0)
  plt.show()

if __name__ == '__main__':
  main()
