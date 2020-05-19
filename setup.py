from setuptools import setup

setup(
    name="dfinder", # Replace with your own username
    version="0.0.1",
    # script=["dfinder.py"],
    author="Christophe Prat",
    author_email="chrisotpheprat@icloud.com",
    url="https://github.com/ChristophePRAT/LinesInDirectory",
    # scripts=["lid.py"],
    python_requires='>=3.6',
    entry_points= {
        'console_scripts': [ 
            'dfinder=dfinder:main' 
        ]   
    }
)