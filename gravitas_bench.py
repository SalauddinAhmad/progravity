"""Backward-compatibility shim forwarding to progravity_bench."""
import sys
from progravity_bench import *

if __name__ == "__main__":
    sys.exit(main())
