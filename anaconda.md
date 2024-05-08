# Anaconda (Python)

```bash
conda create -n [ENVIROMENT_NAME] python=[PYTHON_VERSION]
```
You can append this with packages you want to install.  (`scipy=1.5.4`)

You can also add an ipykernel:

```bash
conda install -c conda-forge ipykernel
python -m ipykernel install --user --name=[ENVIROMENT_NAME]
```

Removing an enviroment:

```bash
conda env remove -n [ENVIROMENT_NAME]
```

Activating or deactivating:

```bash
conda activate [ENVIROMENT_NAME]
conda deactivate
```