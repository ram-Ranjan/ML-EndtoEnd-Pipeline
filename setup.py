from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''Fuction will return List of requirements '''
    requirements: List[str] = []
    with open(file_path,'r') as f:
        for line in f:
            req = line.strip()

            if not req or req.startswith('-e'): 
                continue
            requirements.append(req)
    return requirements
    
setup(
name ="ml_endtoend",
version="0.0.1",
author="Ranjan Kumar",
author_email="ranjan.irl3107@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')    
)

