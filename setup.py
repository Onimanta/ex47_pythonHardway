try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 47 from learnpythonthehardway.org',
    'author': 'Gianni Jacot',
    'url': '',
    'download_url': 'Where to download it.',
    'author_email': 'jacot.gianni@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47_pythonHardway'],
    'scripts': [],
    'name': 'ex47_pythonHardway'
}

setup(**config)
