from setuptools import setup, find_packages


setup(
    name="pyrulatin",
    packages=find_packages(where="src"),
    package_dir={
        "": "src",
    },
    python_requires=">=3.9",
    install_requires=["click", "pygtrie", "pydantic", "PyYAML"],
)
