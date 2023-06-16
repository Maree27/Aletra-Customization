from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in aletra_customizations/__init__.py
from aletra_customizations import __version__ as version

setup(
	name="aletra_customizations",
	version=version,
	description="Customizations",
	author="Umair Akbar",
	author_email="umairakbar34@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
