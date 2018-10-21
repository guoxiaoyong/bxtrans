import itertools
import matplotlib.pyplot as plt
import numpy as np
import sys
import yaml

from common import get_sim_results

symbol_map = {
  'A': '$A$',
  'b': '$b$',
  'p1': '$\pi_1$',
  'C2': '$C_2$',
}

def get_config(case_name):
  with open('cases.yml') as infile:
    config_list = list(yaml.load_all(infile))

  for cfg in config_list:
    if cfg['name'] == case_name:
      config = cfg
      break
  else:
    raise ValueError('case not found!')

  for k, v in config.items():
    if isinstance(v, list):
      label = k
      break

  keys = []
  values = []
  for k, v in config.items():
    keys.append(k)
    values.append(v if isinstance(v, list) else [v])

  res = []
  for v in itertools.product(*values):
    cfg = dict(zip(keys, v))
    cfg['label'] = '%s=%s' % (symbol_map[label], cfg[label])
    res.append(cfg)
  return res


def main():
  markers = itertools.cycle('oD^px')
  configs = get_config(sys.argv[1])
  plt.figure()
  for params in configs:
    res = get_sim_results(**params)
    t = [v['t'] for v in res]
    x = [v['x'] for v in res]
    y = [v['y'] for v in res]
    marker = next(markers)
    plt.plot(t, x, marker=marker, markevery=10, markersize=4, label='$x$, %s' % params['label'])
    plt.plot(t, y, linestyle='--', marker=marker, markevery=10, markersize=4, label='$y$, %s' % params['label'])
  plt.ylabel('$x$ and $y$')
  plt.xlabel('Time($t$)')
  plt.legend(loc='center right')
  plt.grid()
  #plt.xticks(np.arange(0, 31, step=2))
  plt.yticks(np.arange(0, 1.2, step=0.1))
  plt.ylim(0, 1.02)
  plt.xlim(left=0)
  plt.show()


if __name__ == '__main__':
  main()
