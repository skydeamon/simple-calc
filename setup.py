import setuptools

with open("requirements.txt", "r") as fh:
    long_description = fh.read()

packages = [
    "simple_calculator",
]

setuptools.setup(
    name="calculator-pkg-skydeamon",
    version="0.0.1",
    author="skydeamon",
    author_email="skycharmingdeamon@egmail.com",
    description="A simple calculator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Umuzi-org/JADE-JUSTICE-273-simple-calculator-part-1-pythonh",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.2',
)