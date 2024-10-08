from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="spectrumtext",
    version="0.1.2",
    author="Lam",
    author_email="huynhnhathanhtruc@gmail.com",
    description="A library for adding colorful text output to terminal applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamlamm/spectrumtext",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.6",
    install_requires=[],
    extras_require={
        "dev": ["pytest>=3.7"],
    },
)
