contract EthLove {

  // Empty constructor, *Build unstoppable applications* [sic]  
  function EthLove() {}

  // Links are created 
	struct Link {
		string linkerName; // Name of the person that created the link
		address linked;
	}

	event NewLoveLock(address a_, address b_);

	mapping (address => Link) public links;

  function link(string linkerName_, address linked_) {
    if (linked_ == 0) throw;
    if (links[msg.sender].linked != 0) throw; 

    links[msg.sender].linkerName = linkerName_;
    links[msg.sender].linked = linked_;

    if (links[linked_].linked == msg.sender) {
      NewLoveLock(linked_, msg.sender);
    }
  }

  function areLinked(address a_, address b_) returns (bool) {
    return (links[a_].linked == b_ && links[b_].linked == a_);
  }
}