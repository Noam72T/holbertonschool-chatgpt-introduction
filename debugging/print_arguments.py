#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:  # Ignorer sys.argv[0]
        print(arg)
else:
    print("No arguments were provided.")
