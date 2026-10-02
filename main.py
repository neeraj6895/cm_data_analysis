import os

def create_file(file_path):
    """Creates an empty file if it doesn't exist."""
    with open(file_path, 'w') as f:
        pass

def create_project_structure(base_dir):
    # Define the project structure
    structure = {
        "src": {
            "__init__.py": None,
            "ingestion": {
                "__init__.py": None,
                "market_api.py": None,
            },
            "transformations": {
                "__init__.py": None,
                "trade_transform.py": None,
                "position_transform.py": None,
            },
            "jobs": {
                "__init__.py": None,
                "trade_pipeline.py": None,
            },
            "config": {
                "config_loader.py": None,
            },
            "utils": {
                "logger.py": None,
                "spark_utils.py": None,
            },
        },
        "config": {
            "dev.yaml": None,
            "test.yaml": None,
            "prod.yaml": None,
        },
        "data": {
            "raw": {},
            "bronze": {},
            "silver": {},
            "gold": {},
        },
        "tests": {
            "test_trade_transform.py": None,
            "test_position_transform.py": None,
        },
        ".env": None,
        ".env.example": None,
        ".gitignore": None,
        "requirements.txt": None,
        "README.md": None,
        "main.py": None,
    }

    # Recursive function to create directories and files
    def create_structure(base, structure):
        for name, content in structure.items():
            path = os.path.join(base, name)
            if content is None:  # It's a file
                create_file(path)
            else:  # It's a directory
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)

    # Create the base directory and the structure
    os.makedirs(base_dir, exist_ok=True)
    create_structure(base_dir, structure)

# Specify the base directory for the project
base_directory = "cm_data_analysis"
create_project_structure(base_directory)