#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from textwrap import dedent


__version__ = "0.0.0.1"


def main():
    if "--version" in sys.argv[1:]:
        print(__version__)
        exit(0)
    elif "--help" in sys.argv[1:]:
        print("cowsay MESSAGE [MESSAGE]")
        exit(0)

    phrase = " ".join(sys.argv[1:])
    topbar = "-" * len(phrase)
    bottombar = "-" * len(phrase)
    output = dedent(
        """
      %s
    < %s >
      %s
       \   ^__^
        \  (oo)\_______
           (__)\       )\/\\
               ||----w |
               ||     ||
    """
        % (topbar, phrase, bottombar)
    )
    print(output)


if __name__ == "__main__":
    main()
