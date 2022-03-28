import os
import re
import shutil
import sys
from io import open

from setuptools import find_packages, setup

package_name = 'is_likelion'


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version(package_name)

if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    if os.system("twine check dist/*"):
        print("twine check failed. Packages might be outdated.")
        print("Try using `pip install -U twine wheel`.\nExiting.")
        sys.exit()
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree(f"{package_name}.egg-info")
    sys.exit()

setup(
    name='is_likelion',
    version='0.1',
    license='MIT',
    author="shinkeonkim",
    long_description=read('README.rst'),
    author_email='singun11@gmail.com',
    packages=find_packages(exclude=[]),
    package_dir={'': 'src'},
    url='https://github.com/shinkeonkim/is_likelion',
    keywords='likelion',
    python_requires=">=3",
    package_data={},
    zip_safe=False,
)