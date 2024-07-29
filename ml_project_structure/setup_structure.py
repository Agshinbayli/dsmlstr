import os

def create_directory_structure(base_dir):
    dirs = [
        '.github/workflows',
        'data/raw',
        'data/processed',
        'data/external',
        'docs/data_dictionaries',
        'docs/references',
        'docs/reports',
        'models',
        'notebooks',
        'src/data',
        'src/features',
        'src/models',
        'src/visualization',
        'src/utils',
        'tests',
        'configs'
    ]
    
    files = {
        '.github/workflows/ci.yml': '',
        'src/__init__.py': '',
        'src/data/__init__.py': '',
        'src/data/make_dataset.py': '',
        'src/data/preprocess.py': '',
        'src/features/__init__.py': '',
        'src/features/build_features.py': '',
        'src/models/__init__.py': '',
        'src/models/train_model.py': '',
        'src/models/predict_model.py': '',
        'src/visualization/__init__.py': '',
        'src/visualization/visualize.py': '',
        'src/utils/__init__.py': '',
        'src/utils/helpers.py': '',
        'tests/__init__.py': '',
        'tests/test_data.py': '',
        'tests/test_features.py': '',
        'tests/test_models.py': '',
        'configs/model_config.yaml': '',
        'configs/preprocessing_config.yaml': '',
        '.gitignore': '# Add files and directories to be ignored by git',
        'requirements.txt': '# Add project dependencies here',
        'setup.py': '# Setup script for the project',
        'LICENSE': 'MIT License',
        'README.md': '# Project description and setup instructions'
    }

    for dir in dirs:
        os.makedirs(os.path.join(base_dir, dir), exist_ok=True)
    
    for file, content in files.items():
        with open(os.path.join(base_dir, file), 'w') as f:
            f.write(content)

def main():
    base_dir = os.getcwd()
    create_directory_structure(base_dir)
    print("Directory structure created successfully.")

if __name__ == '__main__':
    main()
