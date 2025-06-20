from setuptools import setup, find_packages

setup(
    name="Hojas_excel",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'numpy>=2.3.0',
        'pandas>=2.3.0',
        'python-dateutil>=2.9.0',
        'pytz>=2025.2',
        'tzdata>=2025.2',
        'openpyxl>=3.1.5',
    ],
    author="German Andres Cevallos",
    author_email="germanandrescevallos@gmail.com",
    description="Librería para el análisis de censos ganaderos y cálculo de emisiones",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gercevas/Data-full-analysis.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 
