import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ticketinfo",
    author="OCRV2.0",
    description="Train Delay Investigation",
    # keywords="GNN",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    package_data={"TrainDelayInvestigation.data": ["*.pkl", "*.csv"]},
    version="0.1.0",
    classifiers=[
        # see https://pypi.org/classifiers/
        "Development Status :: 1 - Alpha",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Django==2.2.12",
        "django_debug_toolbar==3.2.4",
        "mysqlclient",
    ],
    extras_require={
        "dev": [
            "mypy",
            "black",
            "flake8-annotations",
        ],
        "tests": [
            "pytest",
            "pytest-dotenv",
        ],
    },
)
