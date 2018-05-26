from setuptools import find_packages, setup

setup(
    name='url_shortener',
    version='1.1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'pytest',
    ],
)