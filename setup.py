from Cython.Build import cythonize
from setuptools import setup, find_packages

setup(
    name='djangoApp',
    version='0.2.3',
    description="A Django App hashed with Cython, which has a 'create_app()' function in the 'djangoApp.wsgi'",
    author='Max',
    author_email='maximadamyan2@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
    ],
    entry_points={
        'wsgi_scripts': [
            'djangoApp = djangoApp.wsgi:create_app',
        ],
    },
    ext_modules=cythonize('djangoApp/**/*.py'),
)
