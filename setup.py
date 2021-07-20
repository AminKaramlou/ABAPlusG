from setuptools import setup, find_packages
install_requires = [
    'click>=8.0.1',
    'pandas>=1.3.0',
    'flask>=2.0.1',
    'flask-Cors>=3.0.10',
    'flask-SocketIO>=5.1.0',
    'eventlet>=0.31.1',
    'gunicorn>=20.1.0'
]
dev_requires = [
    'coverage>=4.4.1',
    'flake8>=3.3.0',
    'pytest>=3.0.7',
    'pytest-mock>=1.6.0',
    'pytest-cov>=2.5.1',
    'pip-tools>=1.10.1',
    'hypothesis>=3.4.5',
]
setup(
    name='bipolar-ABA',
    version='0.0.1',
    url='git@github.com:AminKaram/FYP',
    author='Amin Karamlou',
    author_email='mak514@imperial.ac.uk',
    description='An implementation of the Bipolar-ABA argumentation framework.',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=dev_requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points = '''
    [console_scripts]
    ''',
)
