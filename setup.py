from distutils.core import setup

setup(
     name='pypline-ci',  
     version='0.1.PATCH',
     author="Christian Tragesser",
     author_email="christian@evoen.net",
     description="A docker pipeline library",
     long_description_content_type="text/markdown",
     long_description=open('README.md').read(),
     license='MIT',
     url="https://github.com/christianTragesser/pypline-ci",
     packages=['pyplineCI',],
     install_requires=[
        "docker >= 3.5.0",
    ],
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
