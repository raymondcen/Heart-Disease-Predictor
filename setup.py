from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns list of requirements for package
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements] 
        # list comprehension: [expression for item in iterable if condition]
        
        if HYPHEN_E_DOT in requirements: # should not be in requirements but good safe block
            requirements.remove(HYPHEN_E_DOT)


setup(
name='Heart-Disease-Predictor',
version='0.0.1',
author='Raymond Cen',
author_email='placeholder',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),


)