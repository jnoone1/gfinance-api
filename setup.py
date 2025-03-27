from setuptools import setup, find_packages

setup(
    name="gfinance",  
    version="1.0.0",  
    description="A module to fetch exchange rates and stock values using Google Finance",
    author="Maxichax",
    author_email="33Maxime28@gmail.com",
    url="https://github.com/Maxichax/gfinance-api",  
    packages=find_packages(),  
    install_requires=[
        "beautifulsoup4==4.12.3",
        "soupsieve==2.6"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)