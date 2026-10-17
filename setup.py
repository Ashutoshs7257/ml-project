from setuptools import find_packages , setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS
    '''
    Requirements=[]
    with open(file_path) as file_obj :
        Requirements = file_obj.readlines()
        Requirements=[req.replace("/n","")for req in Requirements]     
        if HYPEN_E_DOT in Requirements:
            Requirements.remove(HYPEN_E_DOT)
            
    return Requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Ashutosh Sharma',
    author_email='ashutoshs72571@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('Requirement.txt')
    
)