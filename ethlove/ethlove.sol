// EthLove -- Love locks on the Ethereum blockchain.
contract EthLove {

  // Empty constructor, *Build unstoppable applications* [sic]  
  function EthLove() {}

  // Links are created when a person calls link()
  // Two reciprocal links create a love lock
	struct Link {
		string linkerName; // Name of the person that created the link
		address linked;    // Address of the person linked with
	}

  // This event is triggered when a love lock is created
	event NewLoveLock(address first, address second);

	mapping (address => Link) public links;

  // Declare a link with another address :
  // - linkerName_ : Name of the person declaring the link (for display only)
  // - linked_ : address of the person that the linker wants to be linked with
  function link(string linkerName_, address linked_) {
    if (linked_ == 0) throw; // probably avoid some tricky issues
    if (links[msg.sender].linked != 0) throw;  // No divorces !

    // Create the link
    links[msg.sender].linkerName = linkerName_;
    links[msg.sender].linked = linked_;

    // If a reciprocal link exist, create the love lock
    if (links[linked_].linked == msg.sender) {
      NewLoveLock(linked_, msg.sender);
    }
  }

  // Convenience accessor to a person name
  function getName(address addr_) constant returns (string) {
    return links[addr_].linkerName;
  }

}