import setuptools 

setuptools.setup(
    version='0.1', 
    name='dictionnaire-francais-malagasy', 
    url ='https://github.com/OsirisJr16/francais_to_malagasy.git' ,
    license = 'MIT' ,
    author = 'OsirisJr' ,
    packages=setuptools.find_packages(),
    install_requires = [
        "requests>=2.28.2" , 
        "bs4>=0.01" ,
    ] ,
    classifiers=[
        "Programming Language :: Python :: 3" , 

    ] , 
    python_requires = '>=3.7'

)
