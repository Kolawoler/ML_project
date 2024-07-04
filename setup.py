from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Function to return a list of requirements from a file."""
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]  # Remove empty lines and strip newline characters
        
        # Remove '-e .' if present
        requirements = [req for req in requirements if req != '-e .']
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Rotimi',
    author_email='Rotimikolawole938@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)