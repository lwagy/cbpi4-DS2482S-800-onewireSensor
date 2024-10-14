from setuptools import setup

setup(name='cbpi4-DS2482S-800-1wireSensor',
      version='0.0.1',
      description='CraftBeerPi Plugin',
      author='Lawrence Wagy',
      author_email='lnwagy@gmail.com',
      url='https://github.com/lwagy/cbpi4-DS2482S-800-1wireSensor',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4_DS2482S_800_1wireSensor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4_DS2482S_800_1wireSensor'],
     )
