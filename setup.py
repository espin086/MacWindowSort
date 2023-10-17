from setuptools import setup, find_packages

setup(
    name="macwindowssort",
    version="0.0.1",
    packages=find_packages(),
    entry_points={"console_scripts": ["macwindowssort = macwindowssort.main:main"]},
    install_requires=open("requirements.txt", encoding="utf-8").readlines(),
)
