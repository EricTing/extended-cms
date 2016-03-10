- [eXtended Contact Mode Score](#sec-1)
- [Requirements](#sec-2)
  - [OpenBabel and Pybel](#sec-2-1)
  - [Pkcombu](#sec-2-2)
  - [APoc](#sec-2-3)
- [Installation](#sec-3)
- [Usage](#sec-4)

# eXtended Contact Mode Score<a id="orgheadline1"></a>

eXtended Contact Mode Score (XCMS) is a novel measure that reliably assess the similarity between two protein-ligand binding conformations.

The design of XCMS allows for comparison even between two non-identical systems,
which makes it more flexible and adaptable compared with traditional methods, such as [RMSD](https://en.wikipedia.org/wiki/Root-mean-square_deviation).

# Requirements<a id="orgheadline5"></a>

## OpenBabel and Pybel<a id="orgheadline2"></a>

We use [OpenBabel](http://openbabel.org/wiki/Main_Page) and its python binding [pybel](https://openbabel.org/docs/dev/UseTheLibrary/Python_Pybel.html) to handle various input formats.

See [here](https://openbabel.org/docs/dev/Installation/install.html#compiling-open-babel) for the instructions how you can compile OpenBabel together with its python binding.

As the instructions require, you must use the old [Eigen2 ](http://eigen.tuxfamily.org/index.php?title=Eigen2)instead of Eigen3.

## Pkcombu<a id="orgheadline3"></a>

We use [pkcombu](http://strcomp.protein.osaka-u.ac.jp/kcombu/doc/README_pkcombu.html) in the KCOMBU package to compare two ligands.

You may download the KCOMBU program [here](http://strcomp.protein.osaka-u.ac.jp/kcombu/download_src.html).

## APoc<a id="orgheadline4"></a>

We use Apoc to compare two binding pockets.

You may donwload Apoc program [here](http://cssb.biology.gatech.edu/APoc).

# Installation<a id="orgheadline6"></a>

If all the requirements are met, then the easiest way to install xcms is to use `pip`.

```sh
$ pip install xcms
```

To install locally

```sh
$ pip install xcms --user
```

# Usage<a id="orgheadline7"></a>

To use it:

```sh
$ x-cms --help
```
