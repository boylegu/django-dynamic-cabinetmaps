import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


__version_info__ = (0, 1, 'dev2')
__version__ = '.'.join([str(v) for v in __version_info__])

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-dynamic-cabinetmaps',
    version=__version__,
    packages=['cabinet_structure'],
    include_package_data=True,
    license='MIT License',
    description='A lightweight dynamic create cabinet graph with django.',
    long_description=README,
    url='https://github.com/boylegu/django-dynamic-cabinetmaps',
    author='BoyleGu',
    author_email='gubaoer@hotmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
