#source: https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
#README.md: https://dillinger.io/

from distutils.core import setup

setup(
  name = 'ChoateStudentHelp',         # How you named your package folder (MyLib)
  packages = ['ChoateStudentHelp'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This module includes 6 distinct functions that I thought would be useful in my life as a student of Choate Rosemary Hall.',   # Give a short description about your library
  author = 'Brian Harder',                   # Type in your name
  author_email = 'bharder23@choate.edu',      # Type in your E-Mail
  url = 'https://github.com/brianHarder/ChoateStudentHelp',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/brianHarder/ChoateStudentHelp/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['useful', 'unique'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'yfinance',
          'stockquotes',
          'sympy',
          'Pillow',
          'geopy',
          'matplotlib',
          'bs4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.9',
  ],
)