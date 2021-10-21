from setuptools import setup

packages = []
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(
    name="modelwatch_app",
    version="0.1.0",
    description="web app to be deployed to aws lambda",
    url="http://github.com/santonaastronomer/modelwatch",
    author="Santona Tuli",
    author_email="santona@astronomer.io",
    license="MIT",
    include_package_data=True,
    install_requires=requirements,
    packages=packages,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)
