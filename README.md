- [eXtended Contact Mode Score](#sec-1)
- [Installation Dependencies](#sec-2)
  - [Python 2.7 and pip](#sec-2-1)
  - [OpenBabel and Pybel](#sec-2-2)
  - [Pkcombu](#sec-2-3)
  - [APoc](#sec-2-4)
- [Installation](#sec-3)
- [Usage](#sec-4)

# eXtended Contact Mode Score<a id="orgheadline1"></a>

Compare two protein-ligand binding conformations even when they are
non-identical systems using **eXtended Contact Mode Score (XCMS)**

# Installation Dependencies<a id="orgheadline6"></a>

## Python 2.7 and pip<a id="orgheadline2"></a>

It is recommended to install [Anaconda](https://www.continuum.io/downloads) on your system to set up the python
working environment, which provides most of the python dependencies to run XCMS,
except for Pybel, whose installation shall be explained below.

## OpenBabel and Pybel<a id="orgheadline3"></a>

We use [OpenBabel](http://openbabel.org/wiki/Main_Page) and its python binding [pybel](https://openbabel.org/docs/dev/UseTheLibrary/Python_Pybel.html) to handle various input formats.

See [here](https://openbabel.org/docs/dev/Installation/install.html#compiling-open-babel) for the instructions how you can compile OpenBabel together with its
python binding.

Be aware, you must use the old [Eigen2 ](http://eigen.tuxfamily.org/index.php?title=Eigen2)instead of Eigen3.

## Pkcombu<a id="orgheadline4"></a>

We use [pkcombu](http://strcomp.protein.osaka-u.ac.jp/kcombu/doc/README_pkcombu.html) in the KCOMBU package to compare two ligands.

You may download the KCOMBU program [here](http://strcomp.protein.osaka-u.ac.jp/kcombu/download_src.html).

Please add the `pkcombu` into your system's `PATH` variable.

## APoc<a id="orgheadline5"></a>

We use Apoc to compare two binding pockets.

You may donwload Apoc program [here](http://cssb.biology.gatech.edu/APoc).

Please add the `apoc` into your system's `PATH` variable.

# Installation<a id="orgheadline7"></a>

At the command line:

```sh
$ pip install xcms
```

To install locally only for yourself:

```sh
$ pip install xcms --user
```

# Usage<a id="orgheadline8"></a>

To use it:

```sh
$ x-cms --help
Usage: x-cms [OPTIONS]

calculated extended contact mode score provided the query and template
protein-ligand structures

Options:
  --template-protein TEXT  template protein file path, in PDB format
  --query-protein TEXT     query protein file path, in PDB format
  --query-ligand TEXT      query ligand file path, in SDF format
  --template-ligand TEXT   template ligand file path, in SDF format
  --help                   Show this message and exit.
```
