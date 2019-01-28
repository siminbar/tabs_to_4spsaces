from setuptools import setup

setup(name='tabs2spaces',
      version='0.1.0',
      packages=['my_project'],
      entry_points={
          'console_scripts': [
              'tabs2spaces = my_project.tabs_to_4spaces:correction'
          ]
      },
     )
