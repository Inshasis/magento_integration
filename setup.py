from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in magento_integration/__init__.py
from magento_integration import __version__ as version

setup(
	name="magento_integration",
	version=version,
	description="Magento 2.0 Two Way Integration With ERPNext",
	author="InshaSiS Technologies",
	author_email="support@inshasis.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
