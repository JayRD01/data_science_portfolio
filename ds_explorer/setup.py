import os
from setuptools import setup, find_packages

def readme() -> str:
    """Reads the README.md for long_description."""
    return open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read()

setup(
    name='data_science_template',
    version='0.1.0',
    author='Jay',
    author_email='...',
    description='A professional and reusable data science project template.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    license='MIT',
    url='https://github.com/JayRD01/data_science_template',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
