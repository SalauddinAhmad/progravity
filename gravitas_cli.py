"""Backward-compatibility shim forwarding to progravity_cli."""
import sys
from progravity_cli import *

if __name__ == "__main__":
    sys.exit(main())
