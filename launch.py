# Copyright 2022 iiPython

# Modules
import os
import sys
from shuttle import app

# Launch server
if __name__ == "__main__":
    app.run(
        host = os.getenv("HOST", "0.0.0.0"),
        port = int(os.getenv("PORT", 8080)),
        debug = os.getenv("DEBUG", "--debug" in sys.argv)
    )
