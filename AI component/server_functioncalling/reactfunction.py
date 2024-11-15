
# Initialize Web3 instance
tokencontractabi = [ { "inputs": [ { "internalType": "uint256", "name": "_keepPercentage", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": True, "internalType": "address", "name": "spender", "type": "address" }, { "indexed": False, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "delegator", "type": "address" }, { "indexed": True, "internalType": "address", "name": "fromDelegate", "type": "address" }, { "indexed": True, "internalType": "address", "name": "toDelegate", "type": "address" } ], "name": "DelegateChanged", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "delegate", "type": "address" }, { "indexed": False, "internalType": "uint256", "name": "previousBalance", "type": "uint256" }, { "indexed": False, "internalType": "uint256", "name": "newBalance", "type": "uint256" } ], "name": "DelegateVotesChanged", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "from", "type": "address" }, { "indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "TokenBurned", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "to", "type": "address" }, { "indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "TokenMinted", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "from", "type": "address" }, { "indexed": True, "internalType": "address", "name": "to", "type": "address" }, { "indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "TokenTransfered", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "from", "type": "address" }, { "indexed": True, "internalType": "address", "name": "to", "type": "address" }, { "indexed": False, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [], "name": "DOMAIN_SEPARATOR", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "approve", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint32", "name": "pos", "type": "uint32" } ], "name": "checkpoints", "outputs": [ { "components": [ { "internalType": "uint32", "name": "fromBlock", "type": "uint32" }, { "internalType": "uint224", "name": "votes", "type": "uint224" } ], "internalType": "struct ERC20Votes.Checkpoint", "name": "", "type": "tuple" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "claimTokens", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "data", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "decimals", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "subtractedValue", "type": "uint256" } ], "name": "decreaseAllowance", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "delegatee", "type": "address" } ], "name": "delegate", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "delegatee", "type": "address" }, { "internalType": "uint256", "name": "nonce", "type": "uint256" }, { "internalType": "uint256", "name": "expiry", "type": "uint256" }, { "internalType": "uint8", "name": "v", "type": "uint8" }, { "internalType": "bytes32", "name": "r", "type": "bytes32" }, { "internalType": "bytes32", "name": "s", "type": "bytes32" } ], "name": "delegateBySig", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "delegates", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getHolderLength", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "blockNumber", "type": "uint256" } ], "name": "getPastTotalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint256", "name": "blockNumber", "type": "uint256" } ], "name": "getPastVotes", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "getVotes", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "addedValue", "type": "uint256" } ], "name": "increaseAllowance", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "nonces", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "numCheckpoints", "outputs": [ { "internalType": "uint32", "name": "", "type": "uint32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" }, { "internalType": "uint256", "name": "deadline", "type": "uint256" }, { "internalType": "uint8", "name": "v", "type": "uint8" }, { "internalType": "bytes32", "name": "r", "type": "bytes32" }, { "internalType": "bytes32", "name": "s", "type": "bytes32" } ], "name": "permit", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "reward", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "s_claimedTokens", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "s_holders", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address payable", "name": "receiver", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "sendTokens", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" } ]
tokencontract_address = "0xd0bcD44A1f11E96C06aBF08f973A775e1c09FecE"
daogovernorcontractaddress ="0xf0Ce7537020C00360ac19C5a657C241b9D5fd47C"
daogovernorcontractabi =[ { "inputs": [ { "internalType": "contract IVotes", "name": "_token", "type": "address" }, { "internalType": "contract TimelockController", "name": "_timelock", "type": "address" }, { "internalType": "uint256", "name": "_votingDelay", "type": "uint256" }, { "internalType": "uint256", "name": "_votingPeriod", "type": "uint256" }, { "internalType": "uint256", "name": "_quorumPercentage", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [], "name": "Empty", "type": "error" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "proposalId", "type": "uint256" } ], "name": "ProposalCanceled", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "proposalId", "type": "uint256" }, { "indexed": False, "internalType": "address", "name": "proposer", "type": "address" }, { "indexed": False, "internalType": "address[]", "name": "targets", "type": "address[]" }, { "indexed": False, "internalType": "uint256[]", "name": "values", "type": "uint256[]" }, { "indexed": False, "internalType": "string[]", "name": "signatures", "type": "string[]" }, { "indexed": False, "internalType": "bytes[]", "name": "calldatas", "type": "bytes[]" }, { "indexed": False, "internalType": "uint256", "name": "startBlock", "type": "uint256" }, { "indexed": False, "internalType": "uint256", "name": "endBlock", "type": "uint256" }, { "indexed": False, "internalType": "string", "name": "description", "type": "string" } ], "name": "ProposalCreated", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "proposalId", "type": "uint256" } ], "name": "ProposalExecuted", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "proposalId", "type": "uint256" }, { "indexed": False, "internalType": "uint256", "name": "eta", "type": "uint256" } ], "name": "ProposalQueued", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "oldProposalThreshold", "type": "uint256" }, { "indexed": False, "internalType": "uint256", "name": "newProposalThreshold", "type": "uint256" } ], "name": "ProposalThresholdSet", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "oldQuorumNumerator", "type": "uint256" }, { "indexed": False, "internalType": "uint256", "name": "newQuorumNumerator", "type": "uint256" } ], "name": "QuorumNumeratorUpdated", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "address", "name": "oldTimelock", "type": "address" }, { "indexed": False, "internalType": "address", "name": "newTimelock", "type": "address" } ], "name": "TimelockChange", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "voter", "type": "address" }, { "indexed": False, "internalType": "uint256", "name": "proposalId", "type": "uint256" }, { "indexed": False, "internalType": "uint8", "name": "support", "type": "uint8" }, { "indexed": False, "internalType": "uint256", "name": "weight", "type": "uint256" }, { "indexed": False, "internalType": "string", "name": "reason", "type": "string" } ], "name": "VoteCast", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "voter", "type": "address" }, { "indexed": False, "internalType": "uint256", "name": "proposalId", "type": "uint256" }, { "indexed": False, "internalType": "uint8", "name": "support", "type": "uint8" }, { "indexed": False, "internalType": "uint256", "name": "weight", "type": "uint256" }, { "indexed": False, "internalType": "string", "name": "reason", "type": "string" }, { "indexed": False, "internalType": "bytes", "name": "params", "type": "bytes" } ], "name": "VoteCastWithParams", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "oldVotingDelay", "type": "uint256" }, { "indexed": False, "internalType": "uint256", "name": "newVotingDelay", "type": "uint256" } ], "name": "VotingDelaySet", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "oldVotingPeriod", "type": "uint256" }, { "indexed": False, "internalType": "uint256", "name": "newVotingPeriod", "type": "uint256" } ], "name": "VotingPeriodSet", "type": "event" }, { "stateMutability": "payable", "type": "fallback" }, { "inputs": [], "name": "BALLOT_TYPEHASH", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "COUNTING_MODE", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [], "name": "EXTENDED_BALLOT_TYPEHASH", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "newMember", "type": "address" } ], "name": "addMember", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "proposalId", "type": "uint256" }, { "internalType": "uint8", "name": "support", "type": "uint8" } ], "name": "castVote", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "proposalId", "type": "uint256" }, { "internalType": "uint8", "name": "support", "type": "uint8" }, { "internalType": "uint8", "name": "v", "type": "uint8" }, { "internalType": "bytes32", "name": "r", "type": "bytes32" }, { "internalType": "bytes32", "name": "s", "type": "bytes32" } ], "name": "castVoteBySig", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "proposalId", "type": "uint256" }, { "internalType": "uint8", "name": "support", "type": "uint8" }, { "internalType": "string", "name": "reason", "type": "string" } ], "name": "castVoteWithReason", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "proposalId", "type": "uint256" }, { "internalType": "uint8", "name": "support", "type": "uint8" }, { "internalType": "string", "name": "reason", "type": "string" }, { "internalType": "bytes", "name": "params", "type": "bytes" } ], "name": "castVoteWithReasonAndParams", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "proposalId", "type": "uint256" }, { "internalType": "uint8", "name": "support", "type": "uint8" }, { "internalType": "string", "name": "reason", "type": "string" }, { "internalType": "bytes", "name": "params", "type": "bytes" }, { "internalType": "uint8", "name": "v", "type": "uint8" }, { "internalType": "bytes32", "name": "r", "type": "bytes32" }, { "internalType": "bytes32", "name": "s", "type": "bytes32" } ], "name": "castVoteWithReasonAndParamsBySig", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "targets", "type": "address[]" }, { "internalType": "uint256[]", "name": "values", "type": "uint256[]" }, { "internalType": "bytes[]", "name": "calldatas", "type": "bytes[]" }, { "internalType": "bytes32", "name": "descriptionHash", "type": "bytes32" } ], "name": "execute", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "payable", "type": "function" }, { "inputs": [], "name": "getMemberLength", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getMembers", "outputs": [ { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getNumberOfProposals", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint256", "name": "blockNumber", "type": "uint256" } ], "name": "getVotes", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint256", "name": "blockNumber", "type": "uint256" }, { "internalType": "bytes", "name": "params", "type": "bytes" } ], "name": "getVotesWithParams", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "proposalId", "type": "uint256" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "hasVoted", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "targets", "type": "address[]" }, { "internalType": "uint256[]", "name": "values", "type": "uint256[]" }, { "internalType": "bytes[]", "name": "calldatas", "type": "bytes[]" }, { "internalType": "bytes32", "name": "descriptionHash", "type": "bytes32" } ], "name": "hashProposal", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "isMember", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "members", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "uint256[]", "name": "", "type": "uint256[]" }, { "internalType": "uint256[]", "name": "", "type": "uint256[]" }, { "internalType": "bytes", "name": "", "type": "bytes" } ], "name": "onERC1155BatchReceived", "outputs": [ { "internalType": "bytes4", "name": "", "type": "bytes4" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "bytes", "name": "", "type": "bytes" } ], "name": "onERC1155Received", "outputs": [ { "internalType": "bytes4", "name": "", "type": "bytes4" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "bytes", "name": "", "type": "bytes" } ], "name": "onERC721Received", "outputs": [ { "internalType": "bytes4", "name": "", "type": "bytes4" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "proposalId", "type": "uint256" } ], "name": "proposalDeadline", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "proposalId", "type": "uint256" } ], "name": "proposalEta", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "proposalId", "type": "uint256" } ], "name": "proposalSnapshot", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "proposalThreshold", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "proposalId", "type": "uint256" } ], "name": "proposalVotes", "outputs": [ { "internalType": "uint256", "name": "againstVotes", "type": "uint256" }, { "internalType": "uint256", "name": "forVotes", "type": "uint256" }, { "internalType": "uint256", "name": "abstainVotes", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "targets", "type": "address[]" }, { "internalType": "uint256[]", "name": "values", "type": "uint256[]" }, { "internalType": "bytes[]", "name": "calldatas", "type": "bytes[]" }, { "internalType": "string", "name": "description", "type": "string" } ], "name": "propose", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "targets", "type": "address[]" }, { "internalType": "uint256[]", "name": "values", "type": "uint256[]" }, { "internalType": "bytes[]", "name": "calldatas", "type": "bytes[]" }, { "internalType": "bytes32", "name": "descriptionHash", "type": "bytes32" } ], "name": "queue", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "blockNumber", "type": "uint256" } ], "name": "quorum", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "quorumDenominator", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "blockNumber", "type": "uint256" } ], "name": "quorumNumerator", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "quorumNumerator", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "target", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" }, { "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "relay", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "member", "type": "address" } ], "name": "removeMember", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "s_proposalCount", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address payable", "name": "receiver", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "sendEther", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "newProposalThreshold", "type": "uint256" } ], "name": "setProposalThreshold", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "newVotingDelay", "type": "uint256" } ], "name": "setVotingDelay", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "newVotingPeriod", "type": "uint256" } ], "name": "setVotingPeriod", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "proposalId", "type": "uint256" } ], "name": "state", "outputs": [ { "internalType": "enum IGovernor.ProposalState", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes4", "name": "interfaceId", "type": "bytes4" } ], "name": "supportsInterface", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "timelock", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "token", "outputs": [ { "internalType": "contract IVotes", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "newQuorumNumerator", "type": "uint256" } ], "name": "updateQuorumNumerator", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "contract TimelockController", "name": "newTimelock", "type": "address" } ], "name": "updateTimelock", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "version", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "votingDelay", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "votingPeriod", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "stateMutability": "payable", "type": "receive" } ]
timelockcontractaddress ="0x3aF5647E366fb51C89e4c43Bc8C173dAa018AFf6"
timelockcontractabi =[ { "inputs": [ { "internalType": "uint256", "name": "minDelay", "type": "uint256" }, { "internalType": "address[]", "name": "proposers", "type": "address[]" }, { "internalType": "address[]", "name": "executors", "type": "address[]" }, { "internalType": "address", "name": "admin", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "bytes32", "name": "id", "type": "bytes32" }, { "indexed": True, "internalType": "uint256", "name": "index", "type": "uint256" }, { "indexed": False, "internalType": "address", "name": "target", "type": "address" }, { "indexed": False, "internalType": "uint256", "name": "value", "type": "uint256" }, { "indexed": False, "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "CallExecuted", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "bytes32", "name": "id", "type": "bytes32" }, { "indexed": True, "internalType": "uint256", "name": "index", "type": "uint256" }, { "indexed": False, "internalType": "address", "name": "target", "type": "address" }, { "indexed": False, "internalType": "uint256", "name": "value", "type": "uint256" }, { "indexed": False, "internalType": "bytes", "name": "data", "type": "bytes" }, { "indexed": False, "internalType": "bytes32", "name": "predecessor", "type": "bytes32" }, { "indexed": False, "internalType": "uint256", "name": "delay", "type": "uint256" } ], "name": "CallScheduled", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "bytes32", "name": "id", "type": "bytes32" } ], "name": "Cancelled", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "oldDuration", "type": "uint256" }, { "indexed": False, "internalType": "uint256", "name": "newDuration", "type": "uint256" } ], "name": "MinDelayChange", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "indexed": True, "internalType": "bytes32", "name": "previousAdminRole", "type": "bytes32" }, { "indexed": True, "internalType": "bytes32", "name": "newAdminRole", "type": "bytes32" } ], "name": "RoleAdminChanged", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "indexed": True, "internalType": "address", "name": "account", "type": "address" }, { "indexed": True, "internalType": "address", "name": "sender", "type": "address" } ], "name": "RoleGranted", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "indexed": True, "internalType": "address", "name": "account", "type": "address" }, { "indexed": True, "internalType": "address", "name": "sender", "type": "address" } ], "name": "RoleRevoked", "type": "event" }, { "inputs": [], "name": "CANCELLER_ROLE", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "DEFAULT_ADMIN_ROLE", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "EXECUTOR_ROLE", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "PROPOSER_ROLE", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "TIMELOCK_ADMIN_ROLE", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "id", "type": "bytes32" } ], "name": "cancel", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "target", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" }, { "internalType": "bytes", "name": "payload", "type": "bytes" }, { "internalType": "bytes32", "name": "predecessor", "type": "bytes32" }, { "internalType": "bytes32", "name": "salt", "type": "bytes32" } ], "name": "execute", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "targets", "type": "address[]" }, { "internalType": "uint256[]", "name": "values", "type": "uint256[]" }, { "internalType": "bytes[]", "name": "payloads", "type": "bytes[]" }, { "internalType": "bytes32", "name": "predecessor", "type": "bytes32" }, { "internalType": "bytes32", "name": "salt", "type": "bytes32" } ], "name": "executeBatch", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [], "name": "getMinDelay", "outputs": [ { "internalType": "uint256", "name": "duration", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" } ], "name": "getRoleAdmin", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "id", "type": "bytes32" } ], "name": "getTimestamp", "outputs": [ { "internalType": "uint256", "name": "timestamp", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "grantRole", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "hasRole", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "target", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" }, { "internalType": "bytes", "name": "data", "type": "bytes" }, { "internalType": "bytes32", "name": "predecessor", "type": "bytes32" }, { "internalType": "bytes32", "name": "salt", "type": "bytes32" } ], "name": "hashOperation", "outputs": [ { "internalType": "bytes32", "name": "hash", "type": "bytes32" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "targets", "type": "address[]" }, { "internalType": "uint256[]", "name": "values", "type": "uint256[]" }, { "internalType": "bytes[]", "name": "payloads", "type": "bytes[]" }, { "internalType": "bytes32", "name": "predecessor", "type": "bytes32" }, { "internalType": "bytes32", "name": "salt", "type": "bytes32" } ], "name": "hashOperationBatch", "outputs": [ { "internalType": "bytes32", "name": "hash", "type": "bytes32" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "id", "type": "bytes32" } ], "name": "isOperation", "outputs": [ { "internalType": "bool", "name": "registered", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "id", "type": "bytes32" } ], "name": "isOperationDone", "outputs": [ { "internalType": "bool", "name": "done", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "id", "type": "bytes32" } ], "name": "isOperationPending", "outputs": [ { "internalType": "bool", "name": "pending", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "id", "type": "bytes32" } ], "name": "isOperationReady", "outputs": [ { "internalType": "bool", "name": "ready", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "uint256[]", "name": "", "type": "uint256[]" }, { "internalType": "uint256[]", "name": "", "type": "uint256[]" }, { "internalType": "bytes", "name": "", "type": "bytes" } ], "name": "onERC1155BatchReceived", "outputs": [ { "internalType": "bytes4", "name": "", "type": "bytes4" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "bytes", "name": "", "type": "bytes" } ], "name": "onERC1155Received", "outputs": [ { "internalType": "bytes4", "name": "", "type": "bytes4" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "bytes", "name": "", "type": "bytes" } ], "name": "onERC721Received", "outputs": [ { "internalType": "bytes4", "name": "", "type": "bytes4" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "renounceRole", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "revokeRole", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "target", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" }, { "internalType": "bytes", "name": "data", "type": "bytes" }, { "internalType": "bytes32", "name": "predecessor", "type": "bytes32" }, { "internalType": "bytes32", "name": "salt", "type": "bytes32" }, { "internalType": "uint256", "name": "delay", "type": "uint256" } ], "name": "schedule", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "targets", "type": "address[]" }, { "internalType": "uint256[]", "name": "values", "type": "uint256[]" }, { "internalType": "bytes[]", "name": "payloads", "type": "bytes[]" }, { "internalType": "bytes32", "name": "predecessor", "type": "bytes32" }, { "internalType": "bytes32", "name": "salt", "type": "bytes32" }, { "internalType": "uint256", "name": "delay", "type": "uint256" } ], "name": "scheduleBatch", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address payable", "name": "receiver", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "sendEther", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes4", "name": "interfaceId", "type": "bytes4" } ], "name": "supportsInterface", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "newDelay", "type": "uint256" } ], "name": "updateDelay", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "stateMutability": "payable", "type": "receive" } ]
nftcontract="0xf579B4BDc91089758F555178044dEfB2Cb21205c"
nftcontractabi=[ { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [ { "internalType": "address", "name": "sender", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" }, { "internalType": "address", "name": "owner", "type": "address" } ], "name": "ERC721IncorrectOwner", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "operator", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "ERC721InsufficientApproval", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "approver", "type": "address" } ], "name": "ERC721InvalidApprover", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "operator", "type": "address" } ], "name": "ERC721InvalidOperator", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "ERC721InvalidOwner", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "receiver", "type": "address" } ], "name": "ERC721InvalidReceiver", "type": "error" }, { "inputs": [ { "internalType": "address", "name": "sender", "type": "address" } ], "name": "ERC721InvalidSender", "type": "error" }, { "inputs": [ { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "ERC721NonexistentToken", "type": "error" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": True, "internalType": "address", "name": "approved", "type": "address" }, { "indexed": True, "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": True, "internalType": "address", "name": "operator", "type": "address" }, { "indexed": False, "internalType": "bool", "name": "approved", "type": "bool" } ], "name": "ApprovalForAll", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "_fromTokenId", "type": "uint256" }, { "indexed": False, "internalType": "uint256", "name": "_toTokenId", "type": "uint256" } ], "name": "BatchMetadataUpdate", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": False, "internalType": "uint256", "name": "_tokenId", "type": "uint256" } ], "name": "MetadataUpdate", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "internalType": "address", "name": "from", "type": "address" }, { "indexed": True, "internalType": "address", "name": "to", "type": "address" }, { "indexed": True, "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "newMember", "type": "address" } ], "name": "addMember", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "approve", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "burn", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "getApproved", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getMemberLength", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "operator", "type": "address" } ], "name": "isApprovedForAll", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "isMember", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "members", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "ownerOf", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "member", "type": "address" } ], "name": "removeMember", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" }, { "internalType": "string", "name": "uri", "type": "string" } ], "name": "safeMint", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" }, { "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "operator", "type": "address" }, { "internalType": "bool", "name": "approved", "type": "bool" } ], "name": "setApprovalForAll", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes4", "name": "interfaceId", "type": "bytes4" } ], "name": "supportsInterface", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "tokenByIndex", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "tokenOfOwnerByIndex", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "tokenURI", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "transferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]
from flask import Flask, request, jsonify
from web3 import Web3
import requests
import json
from llama_cpp_agent.llm_agent import LlamaCppAgent
from llama_cpp_agent.providers.llama_cpp_endpoint_provider import LlamaCppEndpointSettings
from llama_cpp_agent.messages_formatter import MessagesFormatterType
from llama_cpp_agent.function_calling import LlamaCppFunctionTool
from llama_cpp_agent.gbnf_grammar_generator.gbnf_grammar_from_pydantic_models import create_dynamic_model_from_function
from flask_cors import CORS
web3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/29ed729d7617400ab427b75b16c31c63"))




from yeelight import Bulb
def turn_on_light(inner_thoughts: str, command: str) -> str:
    """
    Control the Yeelight bulb.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        command (str): The command to execute "turn on" .
        
    Returns:
        str: A message indicating the action taken.
    """
    bulb_ip = "192.168.31.171"  # IP address of the Yeelight bulb
    bulb = Bulb(bulb_ip)
    bulb.turn_on()
    return f"{inner_thoughts} Light turned on."
    
  

def turn_off_light(inner_thoughts: str, command: str) -> str:
    """
    Control the Yeelight bulb.

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        command (str): The command to execute,  "turn off".
        
    Returns:
        str: A message indicating the action taken.
    """
    bulb_ip = "192.168.31.171"  # IP address of the Yeelight bulb
    bulb = Bulb(bulb_ip)

    bulb.turn_off()
    return f"{inner_thoughts} Light turned off."

def get_eth_balance(address: str) -> float:
    """
    Get the ETH balance of the given Ethereum address.

    Parameters:
        address (str): The Ethereum address for which to retrieve the balance.

    Returns:
        float: The ETH balance of the specified address.
    """
    balance = web3.eth.get_balance(address)
    return web3.from_wei(balance, 'ether')

def get_temperature():
    """
    Fetches the current temperature from the my apartment.

    Returns:
        float: The current temperature.
    """
    api_url = "https://reachsak.pagekite.me/"
    response = requests.get(api_url)
    data = response.json()
    temperature = data['Temperature']
    humidity =data['humidity']
    return f"The temparature is {temperature} degree and the humidity level is {humidity}"

def send_tokens(receiver: str, amount: int) -> str:
    """
    Send Ether from this contract to another contract.

    Parameters:
        receiver (str): The Ethereum address of the receiving contract.
        amount (int): The amount of tokens to be send.

    Returns:
        str: A message indicating the success of the transaction.
    """
    # Assuming this contract has Ether to send
 
 
    contract = web3.eth.contract(address=tokencontract_address, abi=tokencontractabi)
    sender_address = "0xD760A17210b61900F696ad0C21a6e11dc8884198"
    nonce = web3.eth.get_transaction_count(sender_address)
    

    
    sender_account = web3.eth.account.from_key("0886e622999b9ed3cccff106e6fa3a9458fb5c0e310a8e5fa51d3f60e8dff6e3")
    tx_data = contract.functions.transfer(receiver, amount*100000000000000000).build_transaction({
        'nonce': nonce,
        'from': "0xD760A17210b61900F696ad0C21a6e11dc8884198",
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
    })

    signed_tx = web3.eth.account.sign_transaction(tx_data, sender_account._private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return f"Successfully sent {amount} Tokens to contract {receiver}\nTransaction sent. Hash: {tx_hash.hex()}"

def send_eth(receiver: str, amount: int) -> str:
    """
    Send Ether from this contract to another contract.

    Parameters:
        receiver (str): The Ethereum address of the receiving contract.
        amount (int): The amount of Ether to send, in wei.

    Returns:
        str: A message indicating the success of the transaction.
    """
    # Assuming this contract has Ether to send
    sender_address = "0xD760A17210b61900F696ad0C21a6e11dc8884198"
    # sender_account = web3.eth.account.privateKeyToAccount("0886e622999b9ed3cccff106e6fa3a9458fb5c0e310a8e5fa51d3f60e8dff6e3")
    sender_account = web3.eth.account.from_key("0886e622999b9ed3cccff106e6fa3a9458fb5c0e310a8e5fa51d3f60e8dff6e3")
    nonce = web3.eth.get_transaction_count(sender_address)

    tx = {
        'nonce': nonce,
        'to': receiver,
        'value': amount,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
    }
    signed_tx = web3.eth.account.sign_transaction(tx, sender_account._private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return f"Successfully sent {amount/1000000000000000000} ETH to contract {receiver}\nTransaction sent. Hash: {tx_hash.hex()}"



def create_dao_proposal_send_tokens(receiver: str, amount: int) -> str:
    """
    Send Ether from this contract to another contract.

    Parameters:
        receiver (str): The Ethereum address of the receiving contract.
        amount (int): The amount of tokens to be send.

    Returns:
        str: A message indicating the success of the transaction.
    """
    # Assuming this contract has Ether to send
    sender_address = "0xD760A17210b61900F696ad0C21a6e11dc8884198"
    nonce = web3.eth.get_transaction_count(sender_address)
    governor_contract = web3.eth.contract(address=daogovernorcontractaddress, abi=daogovernorcontractabi)
    governance_token_contract = web3.eth.contract(address=tokencontract_address, abi=tokencontractabi)
    encoded_function = governance_token_contract.encodeABI(
        fn_name="sendTokens",
        args=[receiver, amount]
    )
    
    tx_data = governor_contract.functions.propose(
        [tokencontract_address],
        [0],
        [encoded_function],
        "send tokens 1000"
    ).build_transaction({
        'gas': 2000000,  # Adjust gas limit as needed
        'gasPrice': web3.to_wei('50', 'gwei'),  # Adjust gas price as needed
        'from': "0xD760A17210b61900F696ad0C21a6e11dc8884198",
        'nonce': nonce,
    })
    sender_account = web3.eth.account.from_key("0886e622999b9ed3cccff106e6fa3a9458fb5c0e310a8e5fa51d3f60e8dff6e3")
    signed_tx = web3.eth.account.sign_transaction(tx_data, sender_account._private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    proposal_id = governor_contract.events.ProposalCreated().process_receipt(tx_receipt)[-1]['args']['proposalId']
  
    return f"Successfully propose the sending of {amount} Tokens to contract {receiver}\nTransaction Hash: {tx_hash.hex()}\nThe proposal ID is: {proposal_id}"
def queue_proposal(receiver: str, amount: int) -> str:
    """
    Send Ether from this contract to another contract.

    Parameters:
        receiver (str): The Ethereum address of the receiving contract.
        amount (int): The amount of tokens to be send.

    Returns:
        str: A message indicating the success of the transaction.
    """
    # Assuming this contract has Ether to send
    PROPOSAL_DESCRIPTION="send tokens 1000"
    description_hash = Web3.keccak(text=PROPOSAL_DESCRIPTION).hex()
    sender_address = "0xD760A17210b61900F696ad0C21a6e11dc8884198"
    nonce = web3.eth.get_transaction_count(sender_address)
    governor_contract = web3.eth.contract(address=daogovernorcontractaddress, abi=daogovernorcontractabi)
    governance_token_contract = web3.eth.contract(address=tokencontract_address, abi=tokencontractabi)
    encoded_function = governance_token_contract.encodeABI(
        fn_name="sendTokens",
        args=[receiver, amount]
    )
    
    
    tx_data = governor_contract.functions.queue(
        [tokencontract_address],
        [0],
        [encoded_function],
        description_hash
    ).build_transaction({
        'gas': 2000000,  # Adjust gas limit as needed
        'gasPrice': web3.to_wei('50', 'gwei'),  # Adjust gas price as needed
        'from': "0xD760A17210b61900F696ad0C21a6e11dc8884198",
        'nonce': nonce,
    })
    sender_account = web3.eth.account.from_key("0886e622999b9ed3cccff106e6fa3a9458fb5c0e310a8e5fa51d3f60e8dff6e3")
    signed_tx = web3.eth.account.sign_transaction(tx_data, sender_account._private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return f"Successfully queue the proposal of the sending of {amount} Tokens to contract {receiver}\nTransaction Hash: {tx_hash.hex()}"
def execute_proposal(receiver: str, amount: int) -> str:
    """
    Send Ether from this contract to another contract.

    Parameters:
        receiver (str): The Ethereum address of the receiving contract.
        amount (int): The amount of tokens to be send.

    Returns:
        str: A message indicating the success of the transaction.
    """
    # Assuming this contract has Ether to send
    PROPOSAL_DESCRIPTION="send tokens 1000"
    description_hash = Web3.keccak(text=PROPOSAL_DESCRIPTION).hex()
    sender_address = "0xD760A17210b61900F696ad0C21a6e11dc8884198"
    nonce = web3.eth.get_transaction_count(sender_address)
    governor_contract = web3.eth.contract(address=daogovernorcontractaddress, abi=daogovernorcontractabi)
    governance_token_contract = web3.eth.contract(address=tokencontract_address, abi=tokencontractabi)
    encoded_function = governance_token_contract.encodeABI(
        fn_name="sendTokens",
        args=[receiver, amount]
    )
    
    tx_data = governor_contract.functions.execute(
        [tokencontract_address],
        [0],
        [encoded_function],
        description_hash
    ).build_transaction({
        'gas': 2000000,  # Adjust gas limit as needed
        'gasPrice': web3.to_wei('50', 'gwei'),  # Adjust gas price as needed
        'from': "0xD760A17210b61900F696ad0C21a6e11dc8884198",
        'nonce': nonce,
    })
    sender_account = web3.eth.account.from_key("0886e622999b9ed3cccff106e6fa3a9458fb5c0e310a8e5fa51d3f60e8dff6e3")
    signed_tx = web3.eth.account.sign_transaction(tx_data, sender_account._private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return f"Successfully execute the proposal of the sending of {amount} Tokens to contract {receiver}\nTransaction Hash: {tx_hash.hex()}"
def vote_yes_on_proposal(inner_thoughts: str, command: str,proposalid: int) -> str:
    """
    Vote on DAO proposal

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        command (str): The command to execute, either yes or no.
        proposalid (int): The id of the proposal to be voted on.
        
    Returns:
        str: A message indicating the action taken.
    """
  
    sender_address = "0xD760A17210b61900F696ad0C21a6e11dc8884198"
    nonce = web3.eth.get_transaction_count(sender_address)
    governor_contract = web3.eth.contract(address=daogovernorcontractaddress, abi=daogovernorcontractabi)
    vote=1

    if command == "yes":vote=1
    
    tx_data = governor_contract.functions.castVoteWithReason(
            proposalid, vote, inner_thoughts
    ).build_transaction({
        'gas': 2000000,  # Adjust gas limit as needed
        'gasPrice': web3.to_wei('50', 'gwei'),  # Adjust gas price as needed
        'from': "0xD760A17210b61900F696ad0C21a6e11dc8884198",
        'nonce': nonce,
    })
    sender_account = web3.eth.account.from_key("0886e622999b9ed3cccff106e6fa3a9458fb5c0e310a8e5fa51d3f60e8dff6e3")
    signed_tx = web3.eth.account.sign_transaction(tx_data, sender_account._private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return f"Successfully sent vote Yes to the proposal ID {proposalid}\nTransaction sent. Hash: {tx_hash.hex()}\n{inner_thoughts}"

def state_of_the_dao_proposal_with_id(inner_thoughts: str, proposalid: int) -> str:
    """
    Vote on DAO proposal

    Parameters:
        inner_thoughts (str): Inner thoughts to return alongside the action.
        proposalid (int): The id of the proposal to be voted on.
        
    Returns:
        str: A message indicating the action taken.
    """
  
    sender_address = "0xD760A17210b61900F696ad0C21a6e11dc8884198"
    nonce = web3.eth.get_transaction_count(sender_address)
    governor_contract = web3.eth.contract(address=daogovernorcontractaddress, abi=daogovernorcontractabi)
    proposal_state = governor_contract.functions.state(proposalid).call()



    tx_data = governor_contract.functions.state(proposalid).build_transaction({
    'gas': 2000000,  # Adjust gas limit as needed
    'gasPrice': web3.to_wei('50', 'gwei'),  # Adjust gas price as needed
    'from': sender_address,
    'nonce': nonce,})


    sender_account = web3.eth.account.from_key("0886e622999b9ed3cccff106e6fa3a9458fb5c0e310a8e5fa51d3f60e8dff6e3")
    signed_tx = web3.eth.account.sign_transaction(tx_data, sender_account._private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return f"Successfully sent vote Yes to the proposal ID {proposalid}\nTransaction sent. Hash: {tx_hash.hex()}\n{proposal_state }"



##113410437835851053967168896229100919116973723443903734433220654372806990256131
    
  

DynamicSampleModel1 = create_dynamic_model_from_function(send_eth)
DynamicSampleModel2 = create_dynamic_model_from_function(get_eth_balance)
DynamicSampleModel3 = create_dynamic_model_from_function(turn_off_light,"turn off")
DynamicSampleModel4 = create_dynamic_model_from_function(turn_on_light,"turn on")
DynamicSampleModel5 = create_dynamic_model_from_function(get_temperature)
DynamicSampleModel6 = create_dynamic_model_from_function(send_tokens)
DynamicSampleModel7 = create_dynamic_model_from_function(create_dao_proposal_send_tokens)
DynamicSampleModel8 = create_dynamic_model_from_function(vote_yes_on_proposal,"yes")
DynamicSampleModel9 = create_dynamic_model_from_function(state_of_the_dao_proposal_with_id)
DynamicSampleModel10 = create_dynamic_model_from_function(queue_proposal)
DynamicSampleModel11 = create_dynamic_model_from_function(execute_proposal)
function_tools = [LlamaCppFunctionTool(DynamicSampleModel1),LlamaCppFunctionTool(DynamicSampleModel2),LlamaCppFunctionTool(DynamicSampleModel3),LlamaCppFunctionTool(DynamicSampleModel4),LlamaCppFunctionTool(DynamicSampleModel5),LlamaCppFunctionTool(DynamicSampleModel6),LlamaCppFunctionTool(DynamicSampleModel7),LlamaCppFunctionTool(DynamicSampleModel8),LlamaCppFunctionTool(DynamicSampleModel9),LlamaCppFunctionTool(DynamicSampleModel10),LlamaCppFunctionTool(DynamicSampleModel11)]

function_tool_registry = LlamaCppAgent.get_function_tool_registry(function_tools)
system_prompt = "Welcome to the Ethereum System. You can send Ether to another contract address.\n"
main_model = LlamaCppEndpointSettings(
    completions_endpoint_url="http://127.0.0.1:8080/completion"
)
llama_cpp_agent = LlamaCppAgent(main_model, debug_output=True,
                                system_prompt=system_prompt + function_tool_registry.get_documentation(),
                                predefined_messages_formatter_type=MessagesFormatterType.CHATML)

app = Flask(__name__)
CORS(app)

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.json.get('input')  # Assuming input is sent as JSON {"input": "user input here"}
    # Process user input using AI model
    ai_response = llama_cpp_agent.get_chat_response(user_input, temperature=0.3, function_tool_registry=function_tool_registry)
   
    return str(ai_response[0]['return_value'])

if __name__ == '__main__':
    app.run(host='localhost', port=1234, debug=True) 

#64538121593627479219236717456296040253649251070565921025083761489207682213087