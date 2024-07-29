# ml_project_structure

This package creates a structured machine learning project directory.
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

```
## Installation

```sh
pip install -e .

