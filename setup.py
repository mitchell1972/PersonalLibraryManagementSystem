from setuptools import setup, find_packages

setup(
    name='PersonalLibraryManagementSystem',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # list your project's dependencies here, for example:
        # 'requests',
    ],
    entry_points={
        'console_scripts': [
            'run-library=PersonalLibraryManagementSystem.run_library:main',
        ],
    },
)
