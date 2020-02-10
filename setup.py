import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-yash2406", # Replace with your own username
    version="0.0.1",
    author="Yash Aggarwal",
    author_email="yashaggarwal1112@gmail.com",
    description="Library to get nearest neighbours of a point",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yash2406/Geo_Neighbours",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)