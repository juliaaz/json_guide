import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="navigation",
    version="0.0.1",
    author="Julia Maksymiuk",
    author_email="yuliia.maksymyuk@ucu.edu.ua",
    description="Guides user in a json file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juliaaz/json_guide.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)