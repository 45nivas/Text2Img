from setuptools import setup, find_packages

setup(
    name="pythonpackage",                      # Your package name
    version="1.0.0",                           # Package version
    packages=find_packages(),                  # This automatically finds all packages in the project
    install_requires=[                         # Dependencies
        "torch",
        "diffusers",
        "Pillow",
    ],
)
