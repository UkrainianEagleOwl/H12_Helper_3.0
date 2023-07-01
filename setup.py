from setuptools import setup

setup(name='your_simple_helper',
      version='1',
      description='Script helps you with managing contacts.',
      url='https://github.com/UkrainianEagleOwl/H9_Helper',
      author='UkrainianEagleOwl',
      license='MIT',
      packages=['your_simple_helper'],
      entry_points={'console_scripts': [
          'your_simple_helper = your_simple_helper.main:main']}
      )
