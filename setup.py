from setuptools import setup, find_packages
from typing import List

def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("/n","") for req in requirements]
    return requirements
setup(
    name = "ML-PIPLINE PROJECT",
    version = "0.0.1",
    description= "First Project Deployement",
    author= "Zahid Hussain",
    author_email= "zahid.hussain@dsu.edu.pk",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)