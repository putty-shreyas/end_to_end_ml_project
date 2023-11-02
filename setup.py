from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """
    Function returns the list of requirements
    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
name = "end_to_end_ml_project",
version = "0.0.1" ,
author = "Shreyas",
author_email = "putty.shreyas@gmail.com", 
packages = find_packages(),
install_requires = get_requirements("requirements.txt"),
)