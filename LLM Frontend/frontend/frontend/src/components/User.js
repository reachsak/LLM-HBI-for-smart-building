import CssBaseline from "@mui/material/CssBaseline";
import GlobalStyles from "@mui/material/GlobalStyles";
import * as React from "react";
import ethlogo from "./eth.png";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import { useState, useEffect } from "react";
import Stack from "@mui/material/Stack";
import Divider from "@mui/material/Divider";
import { ethers } from "ethers";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import { VoteProposal } from "./VoteBox";
import { ExecuteProposal } from "./ExecuteBox";
import { useGetTotalVoters } from "../web3/GetVotersCount";
import { useGetProposals } from "../web3/GetProposalCount";
import FileUpload from "./FileUpload";
import Upload from "./Upload.json";
import Display from "./Display";
import NFTComponent from "./mmcc";
import "react-awesome-button/dist/styles.css";
import NFTComponentdao from "./mmccdao";
import tokenLogo from "./token_logo.png";
import {
  AwesomeButton,
  AwesomeButtonProgress,
  AwesomeButtonSocial,
} from "react-awesome-button";
export const User = ({
  boxValue,
  getValue,
  userBalance,
  getBalance,
  signer,
  requestFunds,
  createProposal,
  proposal,
  newValue,
  proposalDescription,
}) => {
  const [account, setAccount] = useState("");
  const [contract, setContract] = useState(null);
  const [provider, setProvider] = useState(null);
  const [activeTab, setActiveTab] = useState(0);
  const [shortId, setShortId] = useState();
  const [propDesc, setPropDesc] = useState();
  const [propValue, setPropValue] = useState();

  const { voters, getVoters } = useGetTotalVoters();
  const { proposalCount, getProposalCount } = useGetProposals();
  const [aiText, setAIText] = useState("");
  const [outputText, setOutputText] = useState("");
  const [ethBalance, setEthBalance] = useState(null);

  // Function to update outputText state
  const updateOutputText = (text) => {
    setOutputText(text);
  };
  useEffect(() => {
    // Load DAO balance when component mounts
    handleCheckBalance();
  }, []);
  const handleCheckBalance = async () => {
    try {
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
        const signer = provider.getSigner();
        const address = await signer.getAddress();

        // Call the balance function from the contract to retrieve ETH balance
        const balance = await provider.getBalance(address);

        // Convert balance from Wei to Ether
        const balanceInEth = ethers.utils.formatEther(balance);

        setEthBalance(balanceInEth);
      }
    } catch (error) {
      console.error("Error checking balance:", error);
    }
  };

  const [params, setParams] = useState({
    proposalDescription: localStorage.getItem("proposalDescription") || "",
    proposalAmount: localStorage.getItem("proposalAmount") || 0,
  });

  const requestAndUpdateBalance = async () => {
    await requestFunds(signer);
    await getBalance(signer["_address"]);
  };
  useEffect(() => {
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    const loadProvider = async () => {
      if (provider) {
        window.ethereum.on("chainChanged", () => {
          window.location.reload();
        });

        window.ethereum.on("accountsChanged", () => {
          window.location.reload();
        });
        await provider.send("eth_requestAccounts", []);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setAccount(address);
        let contractAddress = "0x03171560292488897Be175ca23BC2333743c4F1A";

        const contract = new ethers.Contract(
          contractAddress,
          Upload.abi,
          signer
        );
        //console.log(contract);
        setContract(contract);
        setProvider(provider);
      } else {
        console.error("Metamask is not installed");
      }
    };
    provider && loadProvider();
  }, []);

  useEffect(() => {
    getValue();
  }, [boxValue]);
  useEffect(() => {
    setShortId(proposal ? proposal.slice(0, 11) + "..." : "0");
  }, [proposal]);
  useEffect(() => {
    getVoters();
  }, []);
  useEffect(() => {
    getProposalCount();
  }, []);
  useEffect(() => {
    if (signer) {
      getBalance(signer["_address"]);
    }
  }, [signer]);

  const handleParamsChange = (e) => {
    setParams({ ...params, [e.target.name]: e.target.value });
  };
  const sample = () => {
    // Open the URL specified in the gourl function in a new tab
    console.log("placeholder");
  };

  const updateParams = () => {
    setPropDesc(
      proposalDescription
        ? proposalDescription
        : localStorage.getItem("proposalDescription")
    );
    setPropValue(newValue ? newValue : localStorage.getItem("proposalAmount"));
  };

  return (
    <>
      <div>
        <Typography variant="h6" align="center" color="black" component="p">
          <div>
            <div>
              <Stack direction="row" spacing={2} justifyContent="center">
                {/* <Box
                  boxShadow={3}
                  bgcolor="background.paper"
                  p={2}
                  className="retro-box" // Add a class for retro style
                  maxWidth="fit-content" // Set maximum width to fit the content
                  margin="auto" // Center the box horizontally
                  display="flex"
                  flexDirection="column"
                  alignItems="center" // Center the content vertically
                >
                  <p1>My NFT</p1>
                  <NFTComponent account={account} />

                  <Box
                    boxShadow={3}
                    style={{ color: "black" }}
                    bgcolor="background.paper"
                    p={2}
                    className="retro-box" // Add a class for retro style
                    maxWidth="fit-content" // Set maximum width to fit the content
                    margin="auto" // Center the box horizontally
                    display="flex"
                    flexDirection="row"
                    alignItems="center" // Center the content vertically
                  >
                    {" "}
                    <Stack spacing={2} direction="row" justifyContent="center">
                      <AwesomeButton type="linkedin" onPress={sample}>
                        Trade NFT
                      </AwesomeButton>
                      <AwesomeButton type="linkedin" onPress={sample}>
                        Transfer NFT
                      </AwesomeButton>
                      <AwesomeButton type="linkedin" onPress={sample}>
                        Burn NFT
                      </AwesomeButton>
                      <AwesomeButton type="linkedin" onPress={sample}>
                        Transfer NFT
                      </AwesomeButton>
                    </Stack>
                  </Box>
                </Box> */}

                <Box
                  boxShadow={3}
                  bgcolor="background.paper"
                  p={2}
                  className="retro-box" // Add a class for retro style
                  maxWidth="fit-content" // Set maximum width to fit the content
                  margin="auto" // Center the box horizontally
                  display="flex"
                  flexDirection="column"
                  alignItems="center" // Center the content vertically
                >
                  <p1>My Governance Tokens</p1>

                  <span style={{ fontSize: "24px", fontWeight: "bold" }}>
                    {userBalance ? parseInt(userBalance) : "0"}
                  </span>

                  <img
                    src={tokenLogo}
                    alt="Token Logo"
                    style={{ width: "110px", height: "100px" }}
                  />
                  <Box
                    boxShadow={3}
                    style={{ color: "black" }}
                    bgcolor="background.paper"
                    p={2}
                    className="retro-box" // Add a class for retro style
                    maxWidth="fit-content" // Set maximum width to fit the content
                    margin="auto" // Center the box horizontally
                    display="flex"
                    flexDirection="row"
                    alignItems="center" // Center the content vertically
                  >
                    {" "}
                    <Stack spacing={2} direction="row" justifyContent="center">
                      <AwesomeButton type="primary" onPress={sample}>
                        Tranfer Token
                      </AwesomeButton>
                      <AwesomeButton type="danger" onPress={sample}>
                        Trade Token
                      </AwesomeButton>
                    </Stack>
                  </Box>
                </Box>

                <Box
                  boxShadow={3}
                  bgcolor="background.paper"
                  p={2}
                  className="retro-box" // Add a class for retro style
                  maxWidth="200px" // Set maximum width to fit the content
                  margin="auto" // Center the box horizontally
                  display="flex"
                  flexDirection="column"
                  alignItems="center" // Center the content vertically
                >
                  <p1>My Balance</p1>

                  <span style={{ fontSize: "24px", fontWeight: "bold" }}>
                    {ethBalance
                      ? parseFloat(ethBalance).toFixed(3) + " ETH"
                      : "0 ETH"}
                  </span>

                  <div style={{ textAlign: "center", margin: "5px auto" }}>
                    {" "}
                    {/* Adjusted margin */}
                    <img
                      src={ethlogo}
                      alt="Token Logo"
                      style={{ width: "80px", height: "130x" }}
                    />
                  </div>
                  <Box
                    boxShadow={3}
                    style={{ color: "black" }}
                    bgcolor="background.paper"
                    p={2}
                    className="retro-box" // Add a class for retro style
                    maxWidth="fit-content" // Set maximum width to fit the content
                    margin="auto" // Center the box horizontally
                    display="flex"
                    flexDirection="row"
                    alignItems="center" // Center the content vertically
                  >
                    {" "}
                    <AwesomeButton type="primary" onPress={sample}>
                      Tranfer ETH
                    </AwesomeButton>
                  </Box>
                </Box>
              </Stack>
            </div>
            <Box
              boxShadow={3}
              bgcolor="background.paper"
              p={2}
              className="retro-box" // Add a class for retro style
              maxWidth="fit-content" // Set maximum width to fit the content
              margin="auto" // Center the box horizontally
              display="flex"
              flexDirection="column"
              alignItems="center" // Center the content vertically
            >
              <p1>Account Address</p1>
              <span style={{ fontSize: "18px", fontWeight: "bold" }}>
                {account ? account : "0x..."}
              </span>
            </Box>
          </div>
        </Typography>
      </div>
    </>
  );
};
