Compile and deploy a contract
=============================

Example with ethlove (it creates EthLove.js) :

    cd ~/workshop/ethlove
    python3 compile.py ethlove.sol

In geth console :

    loadScript("/home/vagrant/workshop/ethlove/EthLove.js")
    personal.unlockAccount(<YOUR ACCOUNT>)
    var ethlove = deployEthLove()

And then :

    > eth.sendTransaction({from: eth.coinbase, to: eth.accounts[1], value: web3.toWei(1, "ether")})
    "0x8ef..."
    > eth.sendTransaction({from: eth.coinbase, to: eth.accounts[2], value: web3.toWei(1, "ether")})
    "0x6b4..."
    > ethlove.<METHOD>.call(eth.accounts[1], eth.accounts[2])
    false
    > ethlove.<METHOD>.sendTransaction(eth.accounts[1], {from: eth.accounts[2]})
    "0xca2..."
    > ethlove.<METHOD>.call(eth.accounts[1], eth.accounts[2])
    false
    > ethlove.<METHOD>.sendTransaction(eth.accounts[2], {from: eth.accounts[1]})
    "0xd9b..."
    > ethlove.<METHOD>.call(eth.accounts[1], eth.accounts[2])
    true


Develop a web dapp locally
==========================

You need two services running, geth with some rpc options and a web server

In term A:

    cd workshop/ethlove
    python3 -m http.server

In term B:

    geth --dev --rpc --rpccorsdomain "http://localhost:8000" --rpcapi "eth,personal" --datadir /tmp/ethereum_dev_mode

Browse to http://localhost:8000/ethlove.html

If you want to setup a few thing and/or have a JS geth console to test your 
web dapp, you can preload some js :
    
    geth --preload preload.js attach ipc:/tmp/ethereum_dev_mode/geth.ipc