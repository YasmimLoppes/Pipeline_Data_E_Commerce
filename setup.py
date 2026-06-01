from setuptools import setup, find_packages

setup(
    name="pipeline_data_ecommerce",
    version="1.0.0",
    author="Yasmim Lopes",
    author_email="yasmimlopes.dados@gmail.com",
    description="Pipeline completo de dados para E-commerce com qualidade e regras de negócio",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yasmimloppes/Pipeline_Data_E_Commerce",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[
        'requests>=2.31.0',
        'pandas>=2.2.1',
        'numpy>=1.26.4',
        'sqlalchemy>=2.0.28',
        'boto3>=1.34.71',
        'python-dotenv>=1.0.1'
    ],
    entry_points={
        'console_scripts': [
            'pipeline-ecommerce=scripts:main',
        ],
    },
)