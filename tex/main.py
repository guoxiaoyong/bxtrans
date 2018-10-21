import itertools
import matplotlib.pyplot as plt
import numpy as np
import sys
import yaml

from common import get_sim_results


def get_config(case_name):
  with open('cases.yml') as infile:
    config_list = list(yaml.load_all(infile))

  for cfg in config_list:
    if cfg['name'] == case_name:
      config = cfg
      break
  else:
    raise ValueError('case not found!')

  keys = []
  values = []
  for k, v in config.items():
    keys.append(k)
    values.append(v if isinstance(v, list) else [v])

  res = []
  for v in itertools.product(*values):
    res.append(dict(zip(keys, v)))
  return res


def main():
  markers = itertools.cycle('oDs*')
  configs = get_config(sys.argv[1])
  plt.figure()
  for params in configs:
    res = get_sim_results(**params)
    t = [v['t'] for v in res]
    x = [v['x'] for v in res]
    y = [v['y'] for v in res]
    plt.plot(t, x, marker=next(markers))
    plt.plot(t, y, linestyle='--')
  plt.ylabel('$x$')
  plt.xlabel('Time($t$)')
  plt.legend(loc='center right')
  plt.grid()
  plt.show()


if __name__ == '__main__':
  main()
