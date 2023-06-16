"""This module loads environment variables from a .env file or the environment."""


# Load Envirnment Variables from .env File Upon Startup
from dotenv import load_dotenv
load_dotenv()

# Expose `getenv` as a module-level function
from os import getenv