from pathlib import Path

from setuptools import setup, find_packages

readme = (Path(__file__).parent / 'README.md').read_text()
readme = "# "+readme.partition("\n#")[-1]

setup(
  name="commie",
  version="1.0.5",

  author="Art Galkin",
  author_email="ortemeo@gmail.com",
  url='https://github.com/rtmigo/commie',

  packages=find_packages(),
  install_requires=[],

  description="Extracts comments from source code in different programming languages",

  long_description=readme,
  long_description_content_type='text/markdown',

  license='BSD-3-Clause',

  # entry_points={
  #      'console_scripts': [
  #           'allrights = allrights:main',
  #       ]},

  keywords="""
    css python c search java go html sass c-sharp dart bash parser 
    typescript parsing xml comments source-code""".split(),

  # https://pypi.org/classifiers/
  classifiers=[
    "Development Status :: 4 - Beta",
    # "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    'License :: OSI Approved :: BSD License',
    'Topic :: Software Development :: Documentation',
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Operating System :: OS Independent",
  ],

  test_suite='nose.collector',
  tests_require=['nose'],
  zip_safe=False
)