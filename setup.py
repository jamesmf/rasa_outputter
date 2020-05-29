from distutils.core import setup

setup(
    name="RasaOutputter",
    version="0.1.0",
    author="",
    author_email="",
    packages=["rasa_outputter"],
    url="",
    license="LICENSE.txt",
    description="Rasa component for adding pipeline internals to output",
    install_requires=["rasa >= 1.10.0",],
)
