from setuptools import setup

setup(name='tabs2spaces',
      version='0.1.1',
      packages=['main_pack'],
      entry_points={
          'console_scripts': [
              'tabs2spaces = main_pack.__main__:main'
          ]
      },
     )
