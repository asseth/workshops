Compile and deploy a contract
=============================

Requires: python3, solc, geth

Example with ethlove (it creates EthLove.js) :

    python3.5 compile.py ethlove.sol

In geth console :

    loadScript("<PATH>/EthLove.js")
    personal.unlockAccount(<YOUR ACCOUNT>)
    var ethlove = deployEthLove()

And then :

    > eth.sendTransaction({from: eth.coinbase, to: eth.accounts[1], value: web3.toWei(1, "ether")})
    "0x8ef..."
    > eth.sendTransaction({from: eth.coinbase, to: eth.accounts[2], value: web3.toWei(1, "ether")})
    "0x6b4..."
    > ethlove.areLinked.call(eth.accounts[1], eth.accounts[2])
    false
    > ethlove.link.sendTransaction(eth.accounts[1], {from: eth.accounts[2]})
    "0xca2..."
    > ethlove.areLinked.call(eth.accounts[1], eth.accounts[2])
    false
    > ethlove.link.sendTransaction(eth.accounts[2], {from: eth.accounts[1]})
    "0xd9b..."
    > ethlove.areLinked.call(eth.accounts[1], eth.accounts[2])
    true

Attach a console in dev mode
============================

    geth --dev --datadir /tmp/ethereum_dev_mode
    geth attach ipc:/tmp/ethereum_dev_mode/geth.ipc
