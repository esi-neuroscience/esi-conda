# Centrally-Managed conda Environments on the ESI HPC Cluster

The ESI Software Support Group provides a set of pre-configured `conda` environments for
use on the ESI high-performance computing cluster. Every environment is set up
and tested on the institute's cluster with the demands of multiple users in mind.

## Usage

All environments have been assembled and tested on cluster nodes equipped with Intel
Xeon processors running Red Hat Enterprise Linux 8.1 and SLURM 20.02.

### Installation

Setting up an environment requires a recent version of `conda` (4.4+) shipped with
Anaconda or Minoconda, both obtainable from [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html).
Please follow the [official documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#installation)
to install `conda` on your system.
Once `conda` is up and running, you may use any of the provided YAML files
(see [Documentation](#Documentation) for details) to set up the corresponding
environment on your computer by performing the following steps:

1. **Windows**: Open the *Anaconda Prompt* from the *Start* menu\
   **macOS**/**Linux**: open a terminal and add the `conda` command to your shell, i.e.,\
   `source /path/to/conda/etc/profile.d/conda.sh`  (for bash users)\
   `source /path/to/conda/etc/profile.d/conda.csh` (for csh/tcsh users)
2. Create environment from the corresponding YAML file\
   `conda env create --file envs/<ARCHITECTURE/><ENVIRONMENT>.yml`
3. To enable interactive controls for matplotlib figures in Jupyter notebooks,
   the following additional steps are required:
   - Activate the just created environment\
     `conda activate ENVIRONMENT`
   - Install necessary JupyterLab extensions:\
     `jupyter labextension install @jupyter-widgets/jupyterlab-manager`\
     `jupyter labextension install jupyter-matplotlib`
   - Use the command\
     `jupyter labextension list`\
     to ensure that both extensions are "enabled" and "OK"

### Testing

The directory `tests` of this repository contains Python scripts and Jupyter
notebooks to test-drive any created environment. Specifically, Jupyter and its
interactive widgets tend to warrant a quick trial run:

```bash
jupyter lab --ip `hostname` --no-browser --notebook-dir esi-conda/tests/
```

### Trouble-Shooting

All environments have been validated for consistency with respect to dependency
resolution. If `conda` nevertheless complains about conflicting dependencies when
trying to install one of our environments, please open an issue in our
[GitHub issue tracker](https://github.com/esi-neuroscience/esi-conda/issues).

Other than package dependence consistency, interactive figure support in Jupyter
notebooks tends to require some additional tinkering with setting up JupyterLab
extensions and/or `npm` packages. Effective trouble-shooting strongly
depends on the specific hardware platform (CPU architecture, RAM availability) and
the software environment (operating system, `conda` version, `node.js` version etc.).
However, a boilerplate strategy to debug missing interactive figure widgets (*"model not found"* or *"widget loading..."* errors) is to clean up all relevant caches and
re-build the JavaScript components of JupyterLab:

```bash
jlpm cache clean
jupyter lab clean
jupyter nbextension enable --py widgetsnbextension
jupyter lab build
```

Many extensions are still under heavy development and might introduce substantial
changes between releases. It is usually helpful to consult the GitHub issue trackers
of the respective extensions - oftentimes others already ran into similar problems
and have already found workarounds.

## Documentation

All YAML files with names containing the suffix "*_concretized*" have been generated by
exporting the corresponding environments on the ESI HPC cluster. Thus,
`<ENVIRONMENT>_concretized.yml` files can be used to re-create exact clones of ESI compute cluster
environments provided the host system is also a Linux machine. To set up
an environment on another platform, please use the corresponding `<ENVIRONMENT>.yml` file instead,
as outlined in [Installation](#Installation).

Please refer to [the official conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment) for more details about virtual environment management with `conda`.

### Layout

This repository is structured as follows:

- `envs`: contains YAML environment specification files
- `tests`: contains scripts and notebooks to test/try-out environments

### Available environments

- `esi-202xa`/`esi-202xb`: standard "reference" Python environment that is
  updated bi-annually. Comprises most widely used scientific computing packages
  (NumPy, SciPy, matplotlib, pandas, dask, scikit, mne etc.) in their respective
  most recent versions. These environments are provided for both x86 and POWER
  architectures
- `DLC-PPC`: environment for running DeepLabCut on POWER based on a custom fork
