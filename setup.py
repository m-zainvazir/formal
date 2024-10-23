from setuptools import find_packages, setup
from typing import List

hyphen_edot = '_e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Through this func, the list of requirements will be returned
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if hyphen_edot in requirements:
            requirements.remove(hyphen_edot)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Muhammad Zain Vazir',
    author_email='zainvazir1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )