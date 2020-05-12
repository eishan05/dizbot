from setuptools import setup
import dizbot
import sys

def get_requirements():
  with open('requirements.txt') as f:
    install_requires = [line.strip() for line in f]
  if 'win32' in sys.platform.lower():
    install_requires.append('colorama')
  return install_requires

def get_readme():
  with open("README.md") as f:
    return f.read()

setup(
    name="dizbot",
    version=dizbot.__version__,
    description=dizbot.__doc__.strip(),
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    url="https://github.com/eishan05/dizbot",
    author=dizbot.__author__,
    author_email="eishanlawrence5@gmail.com",
    license=dizbot.__license__,
    packages=["dizbot"],
    entry_points={"console_scripts": ["dizbot=dizbot.dizbot:cli"]},
    install_requires=get_requirements(),
        classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=['dizbot', 'discord', 'discord.py', 'bot'],
    python_requires=">=3",
    zip_safe=False,
)
