Welcome to the first Asseth workshop !


Here we provide the skeleton of a dapp that you can use as a starting point 
for your project.

A Dapp needs to be connected to an ethereum node. Let's start one by executing 
the following command in a terminal  :

    geth --dev --rpc --rpccorsdomain "http://localhost:8000" --rpcapi "eth,personal" --datadir /tmp/ethereum_dev_mode

`geth` is a popular ethereum client written in Go. We gave him the `--dev`
option : this tells geth to start in development mode. Instead of coding and testing
our Dapp directly on the main ethereum blockchain (which would be slow and
costly), we will start our own private blockchain starting at Block 0.

Once you are satisfied with your code, the exact same `geth` can be used to
deploy your smart contract on the "real" ethereum blockchain.


To put the solidity smart-contract `ethlove.sol` on our pristine blockchain,
we first need to compile it : 

    cd ~/workshop/ethlove
    python3 compile.py ethlove.sol

`compile.py` is a small python script that use `solc`, the solidity compiler
to compile the contract. Running it creates the file `EthLove.js`, which is
just there to help deploying the contract with `geth`.


To be able to put the contract on the blockchain, we need to : 

- Create an account and make sure there is some ether on it. Since we are on a
private blockchain, we will need to mine it.

- Unlock the account, create and send the contract creation transaction.

Doing so manually each time we are testing our contract would be tedious, we
use preload.js to automatize this :

    geth --preload preload.js attach ipc:/tmp/ethereum_dev_mode/geth.ipc

Wait a few blocks and... congratulations ! You should now have a javascript
console to interact with the blockchain and your contract (if you read
`preload.js` as you should have you know there is an `ethlove` variable that
reference your contract instance).


The `geth` console is very powerful, but not very user friendly. You will
probably want your Dapp to have a nice web front-end.  In the geth console
type `ethlove.address` to know the contract address. You need to edit
ethlove.html, find the `.at("<CONTRACT ADDRESS HERE>")` line and enter your
contract address.

Now open a new terminal and start a http server :

    cd ~/workshop/ethlove
    python3 -m http.server


Open a browser and type in the address `http://localhost:8000/ethlove.html`

The few words you see comes from the ethereum contract you deployed earlier.
Not very impressive, I know. It is now up to you to make it better !


Ressources
==========

- Solidity documentation : https://solidity.readthedocs.io/en/latest/
- Ethereum Javascript API : https://github.com/ethereum/wiki/wiki/JavaScript-API
