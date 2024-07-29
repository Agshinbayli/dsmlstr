# ml_project_structure

Install the Package:

```sh
pip install -e .
```
This will install the dsmlstr package and make the setup_ml_project command available globally.

Run the Script:

now use the package to create the project directory structure; two options to run the script:

Using the command-line tool:


```sh
setup_ml_project
```

Or running the script directly:

```sh
python -m ml_project_structure.setup_structure
```

This will create the specified directory structure in the current working directory.

```
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── docs/
│   ├── data_dictionaries/
│   ├── references/
│   └── reports/
├── models/
├── notebooks/
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── make_dataset.py
│   │   └── preprocess.py
│   ├── features/
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train_model.py
│   │   └── predict_model.py
│   ├── visualization/
│   │   ├── __init__.py
│   │   └── visualize.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_features.py
│   └── test_models.py
├── configs/
│   ├── model_config.yaml
│   └── preprocessing_config.yaml
├── .gitignore
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md

