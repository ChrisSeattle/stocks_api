import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    # 'cryptacular',  # Custome Added for Auth (13)
    'marshmallow_sqlalchemy',  # Custom Added
    'plaster_pastedeploy',
    'psycopg2-binary',  # Custom Added
    'pyramid >= 1.9a',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    # 'pyramid_jwt',  # Custome Added
    'pyramid-restful-framework',  # Custom Added
    'pyramid_retry',
    'pyramid_tm',
    'requests',  # Custom Added
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(
    name='stocks_api',
    version='0.0',
    description='stocks_api',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = stocks_api:main',
        ],
        'console_scripts': [
            'initialize_stocks_api_db = stocks_api.scripts.initializedb:main',
        ],
    },
)
