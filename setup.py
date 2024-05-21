from setuptools import find_packages, setup
from typing import List

hypen_e = '-e .'
def get_req(file:str)-> List[str]:
    requirements = []
    with open(file) as f:
        requirements = f.readlines()
        [req.replace("\n","") for req in requirements]

        if(hypen_e in requirements):
            requirements.remove(hypen_e)



setup(
    name='ML_project',
    version='0.0.1',
    author='Raam Jain',
    author_email='jain.raam@gmail.com',
    packages=find_packages(),
    install_requires= get_req('requirement.txt')
)