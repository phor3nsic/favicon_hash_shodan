from setuptools import setup, find_packages

setup(
    name='favhash',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'mmh3',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'favhash = favhash.favicon:main',
        ],
    },
)