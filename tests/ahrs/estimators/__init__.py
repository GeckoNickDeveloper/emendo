import os
import sys

# Add project root to PYTHONPATH so tests can import the library
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)