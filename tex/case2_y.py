import itertools
import matplotlib.pyplot as plt
import numpy as np

from common import get_sim_results


def main():
  markers = itertools.cycle('oDs*')
  C1 = 2
  A = 0.5
  C2 = 1.8
  b_list = [2, 2.4, 2.6, 3]
  title = '$C_1$=2, $C_2$=1.8, $A$=0.5, $T$=1.1, $a$=0.9, $\pi_1$=2.8, $\pi_2$=4\n$\pi_1 + a + A > \pi_2 - T$'
  plt.figure()
  for b in b_list:
    res = get_sim_results(C2, b, A, dt=0.1, N=100)
    t = [v['t'] for v in res]
    x = [v['x'] for v in res]
    y = [v['y'] for v in res]
    plt.plot(t, y, marker=next(markers), label='$b$=%s' % b)
  plt.title(title)
  plt.ylabel('$y$')
  plt.xlabel('Time($t$)')
  plt.legend(loc='center right')
  plt.grid()
  #plt.xticks(np.arange(0, 31, step=2))
  #plt.yticks(np.arange(0, 1.2, step=0.1))
  plt.ylim(0, 1.02)
  plt.xlim(left=0)
  plt.show()

if __name__ == '__main__':
  main()
