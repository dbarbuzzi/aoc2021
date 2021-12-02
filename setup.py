from setuptools import find_packages, setup

with open("README.md") as f:
    _readme = f.read()

with open("LICENSE") as f:
    _license = f.read()

_dev_deps = [
    "black>=21.11b1",
    "flake8>=4.0.1",
    "isort>=5.10.1",
    "pycln>=1.1.0",
]

setup(
    name="aoc2021",
    version="0.1.0",
    description="Solutions for Advent of Code 2021",
    long_description=_readme,
    author="Domenic Barbuzzi",
    license=_license,
    package_dir={"": "src"},
    packages=find_packages("src", include=("aoc2021", "aoc2021.*"), exclude=("tests")),
    entry_points={
        "console_scripts": ["aoc2021=aoc2021.solve:main"],
    },
    extras_require={
        "dev": _dev_deps,
    },
)
