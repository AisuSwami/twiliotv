
  
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(name='twilio-tv',
      version='.001',
      description='Hatch Twilio-tv',
      long_description=readme,
      author='Naziya Akhthar',
      author_email='nakhthar@twilio.com',
      find_packages=find_packages())