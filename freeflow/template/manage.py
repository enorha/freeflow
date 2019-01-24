#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Command line utility for development and deployment"""
try:
    from freeflow.core.cli import execute
except ImportError as e:
    print(e)
    raise ImportError(
      "Couldn't find Freeflow. Are you sure it's installed?"
    )


def main(argv=None):
    execute(argv)


if __name__ == '__main__':
    main()
