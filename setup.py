from setuptools import setup
import dizbot
import sys

def get_requirements():
  requirements = ["Click", "discord.py"]
  if "win32" in sys.platform.lower():
    requirements.append("colorama")
  return requirements

setup(
    name="dizbot",
    version=dizbot.__version__,
    url="https://github.com/eishan05/dizbot",
    author=dizbot.__author__,
    author_email="eishanlawrence5@gmail.com",
    license=dizbot.__license__,
    packages=["dizbot"],
    entry_points={"console_scripts": ["dizbot=dizbot.dizbot:cli"]},
    install_requires=get_requirements(),
)
