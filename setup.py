import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
     name='pypline-ci',  
     version='0.2.PATCH',
     author="Christian Tragesser",
     author_email="christian@evoen.net",
     description="A docker pipeline library",
     long_description_content_type="text/markdown",
     long_description=read('README.md'),
     license='MIT',
     url="https://github.com/christianTragesser/pypline-ci",
     packages=['pyplineCI',],
     install_requires=[
        "docker >= 3.5.0",
    ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
