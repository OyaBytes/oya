#!/usr/bin/env python
"""
From django
Oya's command-line utility for administrative tasks."""
import os
import sys



def main():
    """Run administrative tasks."""
    os.environ.setdefault('OYA_SETTINGS_MODULE', 'api.settings')
    try:
        from oya.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Oya. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()