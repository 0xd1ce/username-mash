#!/usr/bin/env python
import sys
import os.path

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: {} names.txt domain output.txt".format(sys.argv[0]))
        sys.exit(0)

    if not os.path.exists(sys.argv[1]):
        print("{} not found".format(sys.argv[1]))
        sys.exit(0)

    domain = sys.argv[2]
    output_file = sys.argv[3]

    output_list = []

    with open(output_file, 'w') as f:
        for line in open(sys.argv[1]):
            name = ''.join([c for c in line if c == " " or c.isalpha()])

            tokens = name.lower().split()

            # skip empty lines
            if len(tokens) < 1:
                continue

            fname = tokens[0]
            lname = tokens[-1]

            output_list.append(fname + lname + "@" + domain)
            output_list.append(lname + fname + "@" + domain)
            output_list.append(fname + "." + lname + "@" + domain)
            output_list.append(lname + "." + fname + "@" + domain)
            output_list.append(lname + fname[0] + "@" + domain)
            output_list.append(fname[0] + lname + "@" + domain)
            output_list.append(lname[0] + fname + "@" + domain)
            output_list.append(fname[0] + "." + lname + "@" + domain)
            output_list.append(lname[0] + "." + fname + "@" + domain)
            output_list.append(fname + "@" + domain)
            output_list.append(lname + "@" + domain)

        f.write('\n'.join(output_list))
