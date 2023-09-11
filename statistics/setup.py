from setuptools import setup

setup(
    name='unemployment-statistics',
    version='0.1',
    py_modules=['unemployment_statistics'],
    install_requires=[
        'argparse',
    ],
    entry_points='''
        [console_scripts]
        unemployment-statistics=unemployment_statistics:main
    ''',
)
