#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    conf = os.path.dirname(__file__)
    wafer = os.path.join(conf, '..', 'wafer')
    sys.path.append(wafer)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
