<!--
<p align="center">
  <img src="https://github.com/cthoyt/unittest-templates/raw/main/docs/source/logo.png" height="150">
</p>
-->

<h1 align="center">
  Unittest Templates
</h1>

<p align="center">
    <a href="https://github.com/cthoyt/unittest-templates/actions?query=workflow%3ATests">
        <img alt="Tests" src="https://github.com/cthoyt/unittest-templates/workflows/Tests/badge.svg" />
    </a>
    <a href="https://pypi.org/project/unittest_templates">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/unittest_templates" />
    </a>
    <a href="https://pypi.org/project/unittest_templates">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/unittest_templates" />
    </a>
    <a href="https://github.com/cthoyt/unittest-templates/blob/main/LICENSE">
        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/unittest-templates" />
    </a>
    <a href='https://unit-test-templates.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/unit-test-templates/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href="https://codecov.io/gh/cthoyt/unittest-templates/branch/main">
        <img src="https://codecov.io/gh/cthoyt/unittest-templates/branch/main/graph/badge.svg" alt="Codecov status" />
    </a>  
    <a href="https://github.com/cthoyt/cookiecutter-python-package">
        <img alt="Cookiecutter template from @cthoyt" src="https://img.shields.io/badge/Cookiecutter-snekpack-blue" /> 
    </a>
    <a href='https://github.com/psf/black'>
        <img src='https://img.shields.io/badge/code%20style-black-000000.svg' alt='Code style: black' />
    </a>
    <a href="https://github.com/cthoyt/unittest-templates/blob/main/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg" alt="Contributor Covenant"/>
    </a>
</p>

Write less unittest boilerplate.

## 💪 Getting Started

```python
import abc
from unittest_templates import GenericTestCase, MetaTestCase

# this class defines an interface
class TextProcessorInterface(abc.ABC):
  @abc.abstractmethod
  def process(self, text: str) -> str:
    """Process a text without changing its length."""
    raise NotImplementedError

# we have three concrete implementations
class Lower(Base):
   def process(self, text: str) -> str:
     return bar.lower()

class Upper(Base):
   def process(self, text: str) -> str:
     return bar.upper()
     
class Replace(Base):
   def __init__(self, char: str = "!"):
     self.char = char

   def process(self, text: str) -> str:
     return self.char * len(text)

# we define a generic test case, testing compliance with the interface
class TextProcessorInterfaceTest(GenericTestCase[Interface]):
  def test_process(self):
    text = "Hello World!"
    modified = self.instance.process(text)
    assert len(text) == len(modified)

# without much effort, we can create tests for the implementing classes
class ATest(InterfaceTest):
  cls = A

# we can also add additional specific tests
class BTest(InterfaceTest):
  cls = B
  
  def test_b(self):
    assert self.instance.process("hello") == "HELLO"

class CTest(InterfaceTest):
  cls = C

# we can also test different instantiations
class CTestQuestion(InterfaceTest):
  cls = C
  kwargs = dict(char="?")

# And finally, we can have a test case which makes sure we do not forget any class
class InterfaceMetaTestCase(MetaTestCase[Interface]):
  base_test = InterfaceTest
  base_cls = Interface
```

## 🚀 Installation

The most recent release can be installed from
[PyPI](https://pypi.org/project/unittest_templates/) with:

```bash
$ pip install unittest_templates
```

The most recent code and data can be installed directly from GitHub with:

```bash
$ pip install git+https://github.com/cthoyt/unittest-templates.git
```

## 👐 Contributing

Contributions, whether filing an issue, making a pull request, or forking, are appreciated. See
[CONTRIBUTING.md](https://github.com/cthoyt/unittest-templates/blob/master/.github/CONTRIBUTING.md) for more information on getting involved.

## 👋 Attribution

### ⚖️ License

The code in this package is licensed under the MIT License.

### 🍪 Cookiecutter

This package was created with [@audreyfeldroy](https://github.com/audreyfeldroy)'s
[cookiecutter](https://github.com/cookiecutter/cookiecutter) package using [@cthoyt](https://github.com/cthoyt)'s
[cookiecutter-snekpack](https://github.com/cthoyt/cookiecutter-snekpack) template.

## 🛠️ For Developers

<details>
  <summary>See developer instructions</summary>


The final section of the README is for if you want to get involved by making a code contribution.

### Development Installation

To install in development mode, use the following:

```bash
$ git clone git+https://github.com/cthoyt/unittest-templates.git
$ cd unittest-templates
$ pip install -e .
```

### 🥼 Testing

After cloning the repository and installing `tox` with `pip install tox`, the unit tests in the `tests/` folder can be
run reproducibly with:

```shell
$ tox
```

Additionally, these tests are automatically re-run with each commit in a [GitHub Action](https://github.com/cthoyt/unittest-templates/actions?query=workflow%3ATests).

### 📖 Building the Documentation

The documentation can be built locally using the following:

```shell
$ git clone git+https://github.com/cthoyt/unittest-templates.git
$ cd unittest-templates
$ tox -e docs
$ open docs/build/html/index.html
``` 

The documentation automatically installs the package as well as the `docs`
extra specified in the [`setup.cfg`](setup.cfg). `sphinx` plugins
like `texext` can be added there. Additionally, they need to be added to the
`extensions` list in [`docs/source/conf.py`](docs/source/conf.py).

### 📦 Making a Release

After installing the package in development mode and installing
`tox` with `pip install tox`, the commands for making a new release are contained within the `finish` environment
in `tox.ini`. Run the following from the shell:

```shell
$ tox -e finish
```

This script does the following:

1. Uses [Bump2Version](https://github.com/c4urself/bump2version) to switch the version number in the `setup.cfg`,
   `src/unittest_templates/version.py`, and [`docs/source/conf.py`](docs/source/conf.py) to not have the `-dev` suffix
2. Packages the code in both a tar archive and a wheel using [`build`](https://github.com/pypa/build)
3. Uploads to PyPI using [`twine`](https://github.com/pypa/twine). Be sure to have a `.pypirc` file configured to avoid the need for manual input at this
   step
4. Push to GitHub. You'll need to make a release going with the commit where the version was bumped.
5. Bump the version to the next patch. If you made big changes and want to bump the version by minor, you can
   use `tox -e bumpversion minor` after.
</details>
