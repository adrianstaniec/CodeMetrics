from setuptools import setup

setup(name='codemetrics',
      version='0.1',
      description='Run it on a folder with (unknown) source code to get to know some summary stats about it.',
      url='https://github.com/adrsta/codemetrics',
      author='Adrian Staniec',
      author_email='adrianstaniec@gmail.com',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Documentation',
          'Programming Language :: Python :: 3.6',
      ],
      packages=['codemetrics'],
      install_requires=['pandas', 'colorama', 'PyQt5', 'matplotlib'],
      zip_safe=False)
