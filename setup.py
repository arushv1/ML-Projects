from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements = []
    with open(file_path) as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if not line or line.startswith(('#', '-e')):  # Skip comments, -e ., empty lines
                continue
            requirements.append(line)
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Arush",
    author_email="arushv16@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),

)