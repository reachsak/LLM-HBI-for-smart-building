import { ethers } from "ethers";
import { useState, useEffect } from "react";
import contractAddresses from "../chain-info/deployments/map.json";
import proposalcontractABI from "../chain-info/contracts/ProposalContract.json";

import boxContractABI from "../chain-info/contracts/Box.json";
import SmartBuildingAutomationABI from "../chain-info/contracts/SmartBuildingAutomation.json";
import moralisGovernorABI from "../chain-info/contracts/MoralisGovernor.json";
import TimeLockABI from "../chain-info/contracts/TimeLock.json";
import NFTABI from "../chain-info/contracts/MyToken.json";
import governancetokenABI from "../chain-info/contracts/GovernanceToken.json";
import { useLocalStorage } from "../web3/useLocalStorage";

export function useCreateProposal() {
  const [proposal, setProposal] = useState();
  const [address, setAddress] = useState();
  const [proposalDescription, setProposalDescription] = useState();
  const [newValue, setValue] = useState();
  const [minTemp, setminTemp] = useState();
  const [maxTemp, setmaxTemp] = useState();
  const { setLocalStorage, clearLocalStorage, getLocalStorage } =
    useLocalStorage();

  useEffect(() => {
    if (getLocalStorage("id")) {
      setProposal(getLocalStorage("id"));
    }
  }, []);

  /////////////////////////////////////////////////////////////////////////////////////
  async function createProposal(signer, proposalDescription, value) {
    try {
      clearLocalStorage();
      const proposalcontractaddress =
        contractAddresses["11155111"]["MoralisGovernor"][0];
      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        "0xbf2E408Afa9Bc0E584d976140C08E84d74A56790",
        proposalAbi,
        signer
      );
      const voteTx = await proposalContractInstance.setProposalType(
        "changevalue"
      );
      const voteReceipt = await voteTx.wait(1);
      console.log(voteReceipt);
      const boxContract = contractAddresses["11155111"]["Box"][0];
      // const governancetokencontract =
      //   contractAddresses["11155111"]["GovernanceToken"][0];
      const moralisGovernor =
        contractAddresses["11155111"]["MoralisGovernor"][0];
      const boxAbi = boxContractABI.abi;
      const moralisGovernorAbi = moralisGovernorABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernor,
        moralisGovernorAbi,
        signer
      );
      const boxInterface = new ethers.utils.Interface(boxAbi);
      // const governancetokeninterface = new ethers.utils.Interface(
      //   governancetokenABI
      // );
      const encodedFunction = boxInterface.encodeFunctionData("store", [value]);
      // const encodedFunction2 = boxInterface.encodeFunctionData("sendTokens", [
      //   value,
      // ]);
      // /////
      const proposeTx = await moralisGovernorContractInstance.propose(
        [boxContract],
        [0],
        [encodedFunction],
        proposalDescription,
        { gasLimit: 1000000 }
      );
      // //////
      // const proposeTx2 = await moralisGovernorContractInstance.propose(
      //   [governancetokencontract],
      //   [0],
      //   [encodedFunction2],
      //   proposalDescription,
      //   { gasLimit: 1000000 }
      // );
      // /////
      const proposeReceipt = await proposeTx.wait(3);

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());
      setValue(value);
      setProposalDescription(proposalDescription);

      setLocalStorage("id", proposalId);
      console.log("id", proposalId);
    } catch (err) {
      console.log(err);
    }
  }
  async function cal(signer) {
    let x = signer + 2;
    console.log(x);
  }
  /////////////////////////////////////////////////////////////////////////////////////
  async function createSmartBuildingProposal(
    signer,
    proposalDescription,
    minTemp,
    maxTemp
  ) {
    try {
      // Clear local storage
      clearLocalStorage();

      // Retrieve the contract addresses and ABIs
      const proposalContractAddress =
        contractAddresses["11155111"]["MoralisGovernor"][0];
      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        proposalContractAddress,
        proposalAbi,
        signer
      );

      // Set proposal type (optional, based on your implementation)
      const voteTx = await proposalContractInstance.setProposalType(
        "changeSmartBuildingValues"
      );
      await voteTx.wait(1);

      // Get the SmartBuildingAutomation contract address and ABI
      const smartBuildingAutomationAddress =
        contractAddresses["11155111"]["SmartBuildingAutomation"][0];
      const smartBuildingAutomationAbi = SmartBuildingAutomationABI.abi;
      const smartBuildingAutomationInterface = new ethers.utils.Interface(
        smartBuildingAutomationAbi
      );

      // Encode the function calls to setMinTemperature and setMaxTemperature
      const encodedSetMinTemp =
        smartBuildingAutomationInterface.encodeFunctionData(
          "setMinTemperature",
          [minTemp]
        );
      const encodedSetMaxTemp =
        smartBuildingAutomationInterface.encodeFunctionData(
          "setMaxTemperature",
          [maxTemp]
        );

      // Create a proposal with the encoded function calls
      const moralisGovernorAddress =
        contractAddresses["11155111"]["MoralisGovernor"][0];
      const moralisGovernorAbi = proposalcontractABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernorAddress,
        moralisGovernorAbi,
        signer
      );

      const proposeTx = await moralisGovernorContractInstance.propose(
        [smartBuildingAutomationAddress, smartBuildingAutomationAddress],
        [0, 0],
        [encodedSetMinTemp, encodedSetMaxTemp],
        proposalDescription,
        { gasLimit: 1000000 }
      );
      const proposeReceipt = await proposeTx.wait(3);

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());
      setminTemp(minTemp);
      setmaxTemp(maxTemp);

      setProposalDescription(proposalDescription);

      // Update local state and storage

      setLocalStorage("id", proposalId);
      console.log("Proposal ID:", proposalId);
    } catch (err) {
      console.error(err);
    }
  }

  /////////////////////////////////////////////////////////////////////////////////////
  async function createProposalsendtoken(
    signer,
    proposalDescription,
    value,
    receiverAddress
  ) {
    try {
      clearLocalStorage();

      const proposalcontractaddress =
        contractAddresses["11155111"]["MoralisGovernor"][0];
      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        "0xbf2E408Afa9Bc0E584d976140C08E84d74A56790",
        proposalAbi,
        signer
      );
      const voteTx = await proposalContractInstance.setProposalType(
        "sendtoken"
      );
      const voteReceipt = await voteTx.wait(1);
      console.log(voteReceipt);

      const governancetokencontract =
        contractAddresses["11155111"]["GovernanceToken"][0];
      const moralisGovernor =
        contractAddresses["11155111"]["MoralisGovernor"][0];

      const GovAbi = governancetokenABI.abi;
      const moralisGovernorAbi = moralisGovernorABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernor,
        moralisGovernorAbi,
        signer
      );

      const governancetokeninterface = new ethers.utils.Interface(GovAbi);

      const encodedFunction2 = governancetokeninterface.encodeFunctionData(
        "sendTokens",
        [receiverAddress, value]
      );

      const proposeTx2 = await moralisGovernorContractInstance.propose(
        [governancetokencontract],
        [0],
        [encodedFunction2],
        proposalDescription,
        { gasLimit: 1000000 }
      );

      const proposeReceipt = await proposeTx2.wait(3);
      console.log("it's done");

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());
      setValue(value);
      setAddress(receiverAddress);
      setProposalDescription(proposalDescription);

      setLocalStorage("id", proposalId);
      console.log("id", proposalId);
    } catch (err) {
      console.log(err);
    }
  }
  /////////////////////////////////////////////////////////////////////////////////////
  async function createProposalsendEther(
    signer,
    proposalDescription,
    value,
    receiverAddress
  ) {
    try {
      clearLocalStorage();

      const proposalcontractaddress =
        contractAddresses["11155111"]["MoralisGovernor"][0];
      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        "0xbf2E408Afa9Bc0E584d976140C08E84d74A56790",
        proposalAbi,
        signer
      );
      const voteTx = await proposalContractInstance.setProposalType(
        "sendEther"
      );
      const voteReceipt = await voteTx.wait(1);
      console.log(voteReceipt);

      const TimeLockcontract = contractAddresses["11155111"]["TimeLock"][0];
      const moralisGovernor =
        contractAddresses["11155111"]["MoralisGovernor"][0];

      const TimeLockAbi = TimeLockABI.abi;
      const moralisGovernorAbi = moralisGovernorABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernor,
        moralisGovernorAbi,
        signer
      );

      const TimeLockinterface = new ethers.utils.Interface(TimeLockAbi);

      const encodedFunction2 = TimeLockinterface.encodeFunctionData(
        "sendEther",
        [receiverAddress, value]
      );

      const proposeTx2 = await moralisGovernorContractInstance.propose(
        [TimeLockcontract],
        [0],
        [encodedFunction2],
        proposalDescription,
        { gasLimit: 1000000 }
      );

      const proposeReceipt = await proposeTx2.wait(3);
      console.log("it's done");

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());
      setValue(value);
      setAddress(receiverAddress);
      setProposalDescription(proposalDescription);

      setLocalStorage("id", proposalId);
      console.log("id", proposalId);
    } catch (err) {
      console.log(err);
    }
  }
  /////////////////////////////////////////////////////////////////////////////////////
  async function createProposaladdmember(
    signer,
    proposalDescription,

    receiverAddress
  ) {
    try {
      clearLocalStorage();

      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        "0xbf2E408Afa9Bc0E584d976140C08E84d74A56790",
        proposalAbi,
        signer
      );
      const voteTx = await proposalContractInstance.setProposalType(
        "addMember"
      );
      const voteReceipt = await voteTx.wait(1);
      console.log(voteReceipt);

      const moralisGovernor =
        contractAddresses["11155111"]["MoralisGovernor"][0];

      const moralisGovernorAbi = moralisGovernorABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernor,
        moralisGovernorAbi,
        signer
      );

      const moralisGovernorContractinterface = new ethers.utils.Interface(
        moralisGovernorAbi
      );

      const encodedFunction2 =
        moralisGovernorContractinterface.encodeFunctionData("addMember", [
          receiverAddress,
        ]);

      const proposeTx2 = await moralisGovernorContractInstance.propose(
        [moralisGovernor],
        [0],
        [encodedFunction2],
        proposalDescription,
        { gasLimit: 1000000 }
      );

      const proposeReceipt = await proposeTx2.wait(3);
      console.log("it's done");

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());

      setAddress(receiverAddress);
      setProposalDescription(proposalDescription);

      setLocalStorage("id", proposalId);
      console.log("id", proposalId);
    } catch (err) {
      console.log(err);
    }
  }
  /////////////////////////////////////////////////////////////////////////////////////
  async function createProposalremovemember(
    signer,
    proposalDescription,

    receiverAddress
  ) {
    try {
      clearLocalStorage();

      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        "0xbf2E408Afa9Bc0E584d976140C08E84d74A56790",
        proposalAbi,
        signer
      );
      const voteTx = await proposalContractInstance.setProposalType(
        "removeMember"
      );
      const voteReceipt = await voteTx.wait(1);
      console.log(voteReceipt);

      const moralisGovernor =
        contractAddresses["11155111"]["MoralisGovernor"][0];

      const moralisGovernorAbi = moralisGovernorABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernor,
        moralisGovernorAbi,
        signer
      );

      const moralisGovernorContractinterface = new ethers.utils.Interface(
        moralisGovernorAbi
      );

      const encodedFunction2 =
        moralisGovernorContractinterface.encodeFunctionData("removeMember", [
          receiverAddress,
        ]);

      const proposeTx2 = await moralisGovernorContractInstance.propose(
        [moralisGovernor],
        [0],
        [encodedFunction2],
        proposalDescription,
        { gasLimit: 1000000 }
      );

      const proposeReceipt = await proposeTx2.wait(3);
      console.log("it's done");

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());

      setAddress(receiverAddress);
      setProposalDescription(proposalDescription);

      setLocalStorage("id", proposalId);
      console.log("id", proposalId);
    } catch (err) {
      console.log(err);
    }
  }
  /////////////////////////////////////////////////////////////////////////////////////
  async function createProposalmintnft(
    signer,
    proposalDescription,

    receiverAddress
  ) {
    try {
      clearLocalStorage();

      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        "0xbf2E408Afa9Bc0E584d976140C08E84d74A56790",
        proposalAbi,
        signer
      );
      const voteTx = await proposalContractInstance.setProposalType(
        "removeMember"
      );
      const voteReceipt = await voteTx.wait(1);
      console.log(voteReceipt);

      const moralisGovernor =
        contractAddresses["11155111"]["MoralisGovernor"][0];

      const moralisGovernorAbi = moralisGovernorABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernor,
        moralisGovernorAbi,
        signer
      );

      const moralisGovernorContractinterface = new ethers.utils.Interface(
        moralisGovernorAbi
      );

      const encodedFunction2 =
        moralisGovernorContractinterface.encodeFunctionData("removeMember", [
          receiverAddress,
        ]);

      const proposeTx2 = await moralisGovernorContractInstance.propose(
        [moralisGovernor],
        [0],
        [encodedFunction2],
        proposalDescription,
        { gasLimit: 1000000 }
      );

      const proposeReceipt = await proposeTx2.wait(3);
      console.log("it's done");

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());

      setAddress(receiverAddress);
      setProposalDescription(proposalDescription);

      setLocalStorage("id", proposalId);
      console.log("id", proposalId);
    } catch (err) {
      console.log(err);
    }
  }
  /////////////////////////////////////////////////////////////////////////////////////
  async function createProposalmintnftWC(
    signer,
    proposalDescription,

    receiverAddress
  ) {
    try {
      clearLocalStorage();

      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        "0xbf2E408Afa9Bc0E584d976140C08E84d74A56790",
        proposalAbi,
        signer
      );
      const voteTx = await proposalContractInstance.setProposalType(
        "removeMember"
      );
      const voteReceipt = await voteTx.wait(1);
      console.log(voteReceipt);

      const moralisGovernor =
        contractAddresses["11155111"]["MoralisGovernor"][0];

      const moralisGovernorAbi = moralisGovernorABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernor,
        moralisGovernorAbi,
        signer
      );

      const moralisGovernorContractinterface = new ethers.utils.Interface(
        moralisGovernorAbi
      );

      const encodedFunction2 =
        moralisGovernorContractinterface.encodeFunctionData("removeMember", [
          receiverAddress,
        ]);

      const proposeTx2 = await moralisGovernorContractInstance.propose(
        [moralisGovernor],
        [0],
        [encodedFunction2],
        proposalDescription,
        { gasLimit: 1000000 }
      );

      const proposeReceipt = await proposeTx2.wait(3);
      console.log("it's done");

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());

      setAddress(receiverAddress);
      setProposalDescription(proposalDescription);

      setLocalStorage("id", proposalId);
      console.log("id", proposalId);
    } catch (err) {
      console.log(err);
    }
  }
  /////////////////////////////////////////////////////////////////////////////////////
  async function createProposalmintnftPL(
    signer,
    proposalDescription,

    receiverAddress
  ) {
    try {
      clearLocalStorage();

      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        "0xbf2E408Afa9Bc0E584d976140C08E84d74A56790",
        proposalAbi,
        signer
      );
      const voteTx = await proposalContractInstance.setProposalType(
        "removeMember"
      );
      const voteReceipt = await voteTx.wait(1);
      console.log(voteReceipt);

      const moralisGovernor =
        contractAddresses["11155111"]["MoralisGovernor"][0];

      const moralisGovernorAbi = moralisGovernorABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernor,
        moralisGovernorAbi,
        signer
      );

      const moralisGovernorContractinterface = new ethers.utils.Interface(
        moralisGovernorAbi
      );

      const encodedFunction2 =
        moralisGovernorContractinterface.encodeFunctionData("removeMember", [
          receiverAddress,
        ]);

      const proposeTx2 = await moralisGovernorContractInstance.propose(
        [moralisGovernor],
        [0],
        [encodedFunction2],
        proposalDescription,
        { gasLimit: 1000000 }
      );

      const proposeReceipt = await proposeTx2.wait(3);
      console.log("it's done");

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());

      setAddress(receiverAddress);
      setProposalDescription(proposalDescription);

      setLocalStorage("id", proposalId);
      console.log("id", proposalId);
    } catch (err) {
      console.log(err);
    }
  }
  /////////////////////////////////////////////////////////////////////////////////////
  async function createProposalmintnftUCL(
    signer,
    proposalDescription,

    receiverAddress
  ) {
    try {
      clearLocalStorage();

      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        "0xbf2E408Afa9Bc0E584d976140C08E84d74A56790",
        proposalAbi,
        signer
      );
      const voteTx = await proposalContractInstance.setProposalType(
        "removeMember"
      );
      const voteReceipt = await voteTx.wait(1);
      console.log(voteReceipt);

      const moralisGovernor =
        contractAddresses["11155111"]["MoralisGovernor"][0];

      const moralisGovernorAbi = moralisGovernorABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernor,
        moralisGovernorAbi,
        signer
      );

      const moralisGovernorContractinterface = new ethers.utils.Interface(
        moralisGovernorAbi
      );

      const encodedFunction2 =
        moralisGovernorContractinterface.encodeFunctionData("removeMember", [
          receiverAddress,
        ]);

      const proposeTx2 = await moralisGovernorContractInstance.propose(
        [moralisGovernor],
        [0],
        [encodedFunction2],
        proposalDescription,
        { gasLimit: 1000000 }
      );

      const proposeReceipt = await proposeTx2.wait(3);
      console.log("it's done");

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());

      setAddress(receiverAddress);
      setProposalDescription(proposalDescription);

      setLocalStorage("id", proposalId);
      console.log("id", proposalId);
    } catch (err) {
      console.log(err);
    }
  }
  /////////////////////////////////////////////////////////////////////////////////////
  async function createProposalmintnftEU(
    signer,
    proposalDescription,

    receiverAddress
  ) {
    try {
      clearLocalStorage();

      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        "0xbf2E408Afa9Bc0E584d976140C08E84d74A56790",
        proposalAbi,
        signer
      );
      const voteTx = await proposalContractInstance.setProposalType(
        "removeMember"
      );
      const voteReceipt = await voteTx.wait(1);
      console.log(voteReceipt);

      const moralisGovernor =
        contractAddresses["11155111"]["MoralisGovernor"][0];

      const moralisGovernorAbi = moralisGovernorABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernor,
        moralisGovernorAbi,
        signer
      );

      const moralisGovernorContractinterface = new ethers.utils.Interface(
        moralisGovernorAbi
      );

      const encodedFunction2 =
        moralisGovernorContractinterface.encodeFunctionData("removeMember", [
          receiverAddress,
        ]);

      const proposeTx2 = await moralisGovernorContractInstance.propose(
        [moralisGovernor],
        [0],
        [encodedFunction2],
        proposalDescription,
        { gasLimit: 1000000 }
      );

      const proposeReceipt = await proposeTx2.wait(3);
      console.log("it's done");

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());

      setAddress(receiverAddress);
      setProposalDescription(proposalDescription);

      setLocalStorage("id", proposalId);
      console.log("id", proposalId);
    } catch (err) {
      console.log(err);
    }
  }
  /////////////////////////////////////////////////////////////////////////////////////
  async function createProposalburnnft(
    signer,
    proposalDescription,

    receiverAddress
  ) {
    try {
      clearLocalStorage();

      const proposalAbi = proposalcontractABI.abi;
      const proposalContractInstance = new ethers.Contract(
        "0xbf2E408Afa9Bc0E584d976140C08E84d74A56790",
        proposalAbi,
        signer
      );
      const voteTx = await proposalContractInstance.setProposalType(
        "removeMember"
      );
      const voteReceipt = await voteTx.wait(1);
      console.log(voteReceipt);

      const moralisGovernor =
        contractAddresses["11155111"]["MoralisGovernor"][0];

      const moralisGovernorAbi = moralisGovernorABI.abi;
      const moralisGovernorContractInstance = new ethers.Contract(
        moralisGovernor,
        moralisGovernorAbi,
        signer
      );

      const moralisGovernorContractinterface = new ethers.utils.Interface(
        moralisGovernorAbi
      );

      const encodedFunction2 =
        moralisGovernorContractinterface.encodeFunctionData("removeMember", [
          receiverAddress,
        ]);

      const proposeTx2 = await moralisGovernorContractInstance.propose(
        [moralisGovernor],
        [0],
        [encodedFunction2],
        proposalDescription,
        { gasLimit: 1000000 }
      );

      const proposeReceipt = await proposeTx2.wait(3);
      console.log("it's done");

      const proposalId = proposeReceipt.events[0].args.proposalId;

      const bnValue = ethers.BigNumber.from(proposalId);

      setProposal(bnValue.toString());

      setAddress(receiverAddress);
      setProposalDescription(proposalDescription);

      setLocalStorage("id", proposalId);
      console.log("id", proposalId);
    } catch (err) {
      console.log(err);
    }
  }

  return {
    createProposal,
    createProposalsendtoken,
    createSmartBuildingProposal,
    createProposalsendEther,
    createProposalremovemember,
    createProposaladdmember,
    createProposalmintnft,
    proposal,
    newValue,
    minTemp,
    maxTemp,
    proposalDescription,
    address,
  };
}
