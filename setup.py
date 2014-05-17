from setuptools import setup, find_packages

version = '0.1'

setup(
    name='django-simple-bower',
    version=version,
    description="Integrate bower with django using a template tag",
    long_description=open('README.md').read(),
    classifiers=[
        "Framework :: Django",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    keywords='django, bower',
    author='Ekin Ertaç',
    author_email='ekinertac@gmail.com',
    url='https://github.com/ekinertac/django-simple-bower',
    license='WTFPL',
    packages=['simplebower'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>1.4',
        'django-classy-tags',
    ]
)