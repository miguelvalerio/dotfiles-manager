"""
Main file.
"""

import os
import argparse
from conf import conf
from jinja2 import Environment, FileSystemLoader

basedir = os.path.dirname(os.path.realpath(__file__))
templatedir = os.path.join(basedir, 'templates')
outputdir = os.path.join(basedir, 'output')

parser = argparse.ArgumentParser(description='A simple dotfile manager')
parser.add_argument('-d', '--directory', default=templatedir,
                    help='Directory from which to read templates')
parser.add_argument('-o', '--output', default=outputdir,
                    help='Output directory')
args = parser.parse_args()

env = Environment(loader=FileSystemLoader(args.directory, followlinks=True))
for template in env.list_templates():
    filepath = os.path.join(args.output, template)
    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(env.get_template(template).render(**conf))
print('All templates written')
