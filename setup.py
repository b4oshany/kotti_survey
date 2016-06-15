import os

from setuptools import find_packages
from setuptools import setup

version = '0.1.0'
project = 'kotti_survey'

install_requires = [
    'Kotti>=1.0.0',
    'unidecode'
],

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    CHANGES = ''


setup(
    name=project,
    version=version,
    description="Survey Content Type for Kotti",
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "License :: Repoze Public License",
    ],
    keywords='kotti addon',
    author='Sebastian Brass',
    author_email='brass@xo7.de',
    url='https://github.com/sbabrass/kotti_survey',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    entry_points={
        'fanstatic.libraries': [
            'kotti_survey = kotti_survey.fanstatic:library',
        ],
    },
    package_data={"kotti_survey": ["templates/*",
                                 "static/*",
                                 "locale/*", "views/*",
                                 "alembic/*.*", "alembic/versions/*"]},
    extras_require={}
)
