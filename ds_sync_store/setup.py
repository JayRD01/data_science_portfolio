import os
from setuptools import setup, find_packages

def readme() -> str:
    """Reads the README.md for long_description."""
    return open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read()

setup(
    name='ds_sync_store',
    version='0.1.0',
    author='JayRD',
    author_email='...',
    description='DS_Sync_Store is a minimal Python project that uses SQLAlchemy with the Singleton pattern to manage product data, while demonstrating asyncio, threading, and multiprocessing for concurrent access.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    license='MIT',
    url='https://github.com/JayRD01/ds_sync_store',
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
