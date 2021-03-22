<!--
<p align="center">
  <img src="docs/source/logo.png" height="150">
</p>
-->

<h1 align="center">
  Unit Test Templates
</h1>

<p align="center">
    <a href="https://github.com/cthoyt/unittest-templates/actions/workflows/tests.yml">
        <img alt="Tests" src="https://github.com/cthoyt/unittest-templates/actions/workflows/tests.yml/badge.svg" />
    </a>
    <a href="https://github.com/cthoyt/cookiecutter-python-package">
        <img alt="Cookiecutter template from @cthoyt" src="https://img.shields.io/badge/Cookiecutter-python--package-yellow" /> 
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
    <a href="https://zenodo.org/badge/latestdoi/350466742">
      <img src="https://zenodo.org/badge/350466742.svg" alt="DOI">
    </a>
</p>

Write less unittest boilerplate.

## ⬇️ Installation

The most recent release can be installed from
[PyPI](https://pypi.org/project/unittest_templates/) with:

```bash
$ pip install unittest_templates
```

The most recent code and data can be installed directly from GitHub with:

```bash
$ pip install git+https://github.com/cthoyt/unittest-templates.git
```

To install in development mode, use the following:

```bash
$ git clone git+https://github.com/cthoyt/unittest-templates.git
$ cd unittest-templates
$ pip install -e .
```

## ⚖️ License

The code in this package is licensed under the MIT License.

## 🙏 Contributing
Contributions, whether filing an issue, making a pull request, or forking, are appreciated. See
[CONTRIBUTING.rst](https://github.com/cthoyt/unittest-templates/blob/master/CONTRIBUTING.rst) for more information on getting
involved.

## 🍪 Cookiecutter Acknowledgement

This package was created with [@audreyfeldroy](https://github.com/audreyfeldroy)'s
[cookiecutter](https://github.com/cookiecutter/cookiecutter) package using [@cthoyt](https://github.com/cthoyt)'s
[cookiecutter-python-package](https://github.com/cthoyt/cookiecutter-python-package) template.

## 🛠️ Development

The final section of the README is for if you want to get involved by making a code contribution.

### ❓ Testing

After cloning the repository and installing `tox` with `pip install tox`, the unit tests in the `tests/` folder can be
run reproducibly with:

```shell
$ tox
```

Additionally, these tests are automatically re-run with each commit in a [GitHub Action](https://github.com/cthoyt/unittest-templates/actions?query=workflow%3ATests).

### 📦 Making a Release

After installing the package in development mode and installing
`tox` with `pip install tox`, the commands for making a new release are contained within the `finish` environment
in `tox.ini`. Run the following from the shell:

```shell
$ tox -e finish
```

This script does the following:

1. Uses BumpVersion to switch the version number in the `setup.cfg` and
   `src/unittest_templates/version.py` to not have the `-dev` suffix
2. Packages the code in both a tar archive and a wheel
3. Uploads to PyPI using `twine`. Be sure to have a `.pypirc` file configured to avoid the need for manual input at this
   step
4. Push to GitHub. You'll need to make a release going with the commit where the version was bumped.
5. Bump the version to the next patch. If you made big changes and want to bump the version by minor, you can
   use `tox -e bumpversion minor` after.
