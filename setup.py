from setuptools import setup, find_namespace_packages

setup(name='clean',
      version='2.0',
      description='Sorts files in a folder with threads and processes',
      url='https://github.com/DanielDDZ/clean_folder.2.0',
      author='Daniel Zubov',
      author_email='danielzubov12@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': [
          'clean-folder = clean_folder.clean:main']}
      )
