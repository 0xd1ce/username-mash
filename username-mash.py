#!/usr/bin/env python
import sys
import os.path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: {} names.txt domain".format(sys.argv[0]))
        sys.exit(0)

    if not os.path.exists(sys.argv[1]):
        print("{} not found".format(sys.argv[1]))
        sys.exit(0)

    domain = sys.argv[2]

    for line in open(sys.argv[1]):
        name = ''.join([c for c in line if c == " " or c.isalpha()])

        tokens = name.lower().split()

        # skip empty lines
        if len(tokens) < 1:
            continue

        fname = tokens[0]
        lname = tokens[-1]

        print(fname + lname + "@" + domain)           # johndoe@domain
        print(lname + fname + "@" + domain)           # doejohn@domain
        print(fname + "." + lname + "@" + domain)     # john.doe@domain
        print(lname + "." + fname + "@" + domain)     # doe.john@domain
        print(lname + fname[0] + "@" + domain)        # doej@domain
        print(fname[0] + lname + "@" + domain)        # jdoe@domain
        print(lname[0] + fname + "@" + domain)        # djoe@domain
        print(fname[0] + "." + lname + "@" + domain)  # j.doe@domain
        print(lname[0] + "." + fname + "@" + domain)  # d.john@domain
        print(fname + "@" + domain)                   # john@domain
        print(lname + "@" + domain)                   # joe@domain
