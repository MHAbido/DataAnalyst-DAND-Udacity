from setuptools import setup
import sys

version = '0.3.0'
install_requires = []

if sys.version_info[:2] < (3, 4):
    install_requires.append('enum34')

setup(name='beautifultable',
      version=version,
      description='Utility package to print visually appealing ASCII tables to terminal',
      install_requires=install_requires,
      long_description=open('README.rst', 'rt').read(),
      author='Priyam Singh',
      author_email='priyamsingh.22296@gmail.com',
      packages=['beautifultable'],
      url='https://github.com/pri22296/beautifultable',
      download_url='https://github.com/pri22296/beautifultable/tarball/{}'.format(version),
      keywords='table terminal ascii',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Printing',
          'Topic :: Text Processing',
      ],
)
