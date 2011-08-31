from setuptools import setup, find_packages

setup(
    name='django-css-mixin',
    version='0.0.1',
    description="""A simple Django model mixin to specify id, class, or style
    attributes for CSS styling""",
    long_description=open("README.rst",'r').read(),
    zip_safe=False,
    packages=find_packages(),
) 
