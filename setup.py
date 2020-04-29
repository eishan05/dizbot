from setuptools import setup
import dizbot

setup(
    name="dizbot",
    version=dizbot.__version__,
    url="https://github.com/eishan05/dizbot",
    author=dizbot.__author__,
    author_email="eishanlawrence5@gmail.com",
    license=dizbot.__license__,
    packages=["dizbot"],
    entry_points={"console_scripts": ["dizbot=dizbot.__main__:main"]},
    install_requires=[
      "Click",
    ],
)
