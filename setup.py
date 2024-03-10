from setuptools import setup, find_packages

setup(
    name='django_db_seed',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'django_db_seed': ['management/commands/*.py'],
    },
    install_requires=[
        'Django>=5.0.3',
        # Add any other dependencies here
    ],
    python_requires='>=3.12',
    license='MIT',
    description='A Django app to backup and restore the database.',
    long_description=open('README.md').read(),
    url='https://github.com/AfzalSabbir/django_db_seed',
    author='Afzalur Rahman Sabbir',
    author_email='afzalbd1@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 5.0.3',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
