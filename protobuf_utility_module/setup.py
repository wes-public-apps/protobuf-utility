from setuptools import setup, find_packages


tests_requires = []

dev_requires = [] + tests_requires

setup(
    name="protobuf-utility",
    version="0.1.0",
    description='''
    A utility providing limited infrastructure for managing data objects created utilizing google's
    protobuf.
    ''',
    author='Wesley Murray',
    author_email='murraywj97@gmail.com',
    license='MIT',
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="protobuf schema sql migration graphql logging",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "protobuf == 4.21.6"
    ],
    tests_require=tests_requires,
    extras_require={
        'test': tests_requires,
        'dev': dev_requires,
    },
    include_package_data=True,
)