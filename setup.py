from setuptools import setup, find_packages

setup(
    name='ml_project_structure',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'setup_ml_project=ml_project_structure.setup_structure:main',
        ],
    },
    include_package_data=True,
    install_requires=[],
    author='AgshinBayli',
    author_email='aqsinbeyli@gmail.com',
    description='A package to create a structured machine learning project directory.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Agshinbayli/dsmlstr',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
