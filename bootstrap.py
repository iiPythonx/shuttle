# Copyright 2022 iiPython

# Modules
import os
import logging

# Logging setup
logging.basicConfig(
    format = "[Shuttle %(levelname)s] :: %(message)s",
    level = logging.INFO
)

# Handle directory creation
# Created with os.makedirs, so no parent directories need to be listed here
needed_dirs = [
    "data/db"
]
for d in needed_dirs:
    d = os.path.join(os.path.dirname(__file__), d)
    if os.path.isdir(d):
        continue

    os.makedirs(d)
    logging.info(f"Created {d}")
