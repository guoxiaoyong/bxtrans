from setuptools import setup

setup(name='bxtrans',
      version='0.0.1',
      packages=['bxtrans'],
      url='www.github.com/guoxiaoyong/bxtrans',
      license='GPL',
      author='Xiaoyong Guo',
      author_email='guoxiaoyong@guoxiaoyong.com',
      description="Xiaoyong's personal tool.",
      entry_points={
          'gui_scripts': ['bxtrans = bxtrans.bxtrans:main']
      }
)
