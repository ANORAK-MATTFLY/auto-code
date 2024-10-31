from setuptools import setup, find_packages

def read_requirement():
    with open("requirements.txt") as required:
        content = required.read()
        requirements = content.split("\n")
    return requirements


setup(
    name="auto-code",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirement(),
    entry_points='''
    [console_scripts]
    auto-code=auto_code.cli:cli
    '''
)
