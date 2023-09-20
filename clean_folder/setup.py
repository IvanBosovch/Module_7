from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.1.0',
      description='clean_folder',
      author='Ivan_Bosovych',
      author_email='bosovych58470@gmail.com',
      license='MIT',
      classifiers=[
          'Programming language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent'],
      packages=find_namespace_packages(),
      entry_points={'console_scripts': [
          'clean_folder=clean_folder.clean:main']}
      )
