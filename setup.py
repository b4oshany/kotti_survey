import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    CHANGES = ''

version = "0.2.8"

install_requires = [
    'Kotti>=1.0.0',
    'user-agents>=1.0.1',
    'kotti_analytics>=0.2',
    'unidecode',
    'psycopg2'
]


setup(
    name='kotti_survey',
    version=version,
    description="PDF content type for Kotti",
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Repoze Public License",
    ],
    author='Oshane Bailey',
    author_email='b4.oshany@gmail.com',
    url='https://github.com/b4oshany/kotti_survey',
    keywords='kotti web cms wcms pylons pyramid sqlalchemy bootstrap pdf',
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    dependency_links=[],
    entry_points={
        'fanstatic.libraries': [
            'kotti_survey = kotti_survey.fanstatic:library',
        ],
    },
    package_data={"kotti_survey": ["templates/*", "static/*",
                                   "locale/*", "views/*",
                                   "alembic/*.*", "alembic/versions/*"]},
    extras_require={},
)
