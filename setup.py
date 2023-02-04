from setuptools import setup

try:
	import pypandoc
	long_description = pypandoc.convert_file('README.md', 'rst')
	long_description = long_description.replace("\r","") 
except(IOError, ImportError):
	long_description = open('README.md').read()

setup(name='crackertool',
version='0.2',
description='A PIP FOR INSTALLING CRACKER-TOOL OF CRACKER911181',
license="MIT",
long_description=long_description,
long_description_content_type='text/markdown',
author='cracker911181',
author_email='admin@cracker911181.cf',
url='https://pypi.org/project/crackertool',
download_url='https://pypi.org/project/crackertool',
packages=['crackertool'],

zip_safe=False)
