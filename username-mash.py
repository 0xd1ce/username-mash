#!/usr/bin/env python
import sys
import os.path
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input file containing names", required=True)
    parser.add_argument("--domain", help="domain for email addresses", required=True)
    parser.add_argument("--output", help="output file for generated email addresses", required=True)
    args = parser.parse_args()

    input_file = args.input
    domain = args.domain
    output_file = args.output

    if not os.path.exists(input_file):
        print("{} not found".format(input_file))
        sys.exit(0)

    output_list = []

    with open(output_file, 'w') as f:
        for line in open(input_file):
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
