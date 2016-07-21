import argparse
import json
import subprocess
import sys


def compile_solidity(src_path):
    # Python 3.5 only
    output = subprocess.check_output(['solc', src_path, '--combined-json', 'abi,bin'])
    return json.loads(output.decode('utf-8'))['contracts']

def format_js(contracts):
    return '\n'.join(["var {} = {};".format(name, abi_bin)
                      for name, abi_bin in contracts.items()])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Compile a solidity contract & create a loadScript-able js')
    parser.add_argument('src', help="solidity source")

    args = parser.parse_args()
    contracts = compile_solidity(args.src)
    template = open('deploy_template.js').read()

    for name, abi_bin in contracts.items():
        with open(name+'.js', 'w') as f:
            f.write(template.format(name=name, abi_bin=abi_bin))
