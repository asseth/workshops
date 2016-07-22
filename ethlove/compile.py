import argparse
import json
import subprocess
import sys


_TEMPLATE = """
var {name}AbiBin = {abi_bin};

var {name}Contract = web3.eth.contract(JSON.parse({name}AbiBin.abi));

function deploy{name}() {{
    console.log('deploying {name} contract...')
    // Pass constructor arguments to new if necessary 
    return {name}Contract.new(
        {{from:eth.coinbase, data: {name}AbiBin.bin, gas: 1000000}},
        function(error, contract){{
            if (error) {{
                console.error(error);
                return;
            }}
            if(!contract.address) {{
                console.log(
                    "contract {name} creation transaction: " +
                        contract.transactionHash);
            }} else {{
                console.log("contract {name} mined! Address: " + contract.address);
            }}
        }});
}}
"""


def compile_solidity(src_path):
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

    for name, abi_bin in contracts.items():
        with open(name+'.js', 'w') as f:
            f.write(_TEMPLATE.format(name=name, abi_bin=abi_bin))
