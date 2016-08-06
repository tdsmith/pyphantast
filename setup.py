from setuptools import setup

versionfile = 'phantast/version.py'
exec(compile(open(versionfile, 'rb').read(), versionfile, 'exec'))

setup(
    name='pyphantast',
    version=__version__,  # noqa
    url='https://github.com/tdsmith/ijroi',
    license='MIT',
    author='Tim D. Smith',
    author_email='pypi@tds.xyz',
    description='PHANTAST implementation',
    packages=['phantast'],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ],
    install_requires=['numpy', 'scipy'],
    entry_points={'console_scripts': ['phantast=phantast.__main__:main']},
)
