from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='sampleproject',
    version='0.0.0',
    description='Python project for shelf organisation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='L. Penjin'
    )
