import React, { useEffect, useState, useRef } from "react";
import Box from "@mui/material/Box";
import "./Display.css";
import { ethers } from "ethers";
import axios from "axios";
import {
  AwesomeButton,
  AwesomeButtonProgress,
  AwesomeButtonSocial,
} from "react-awesome-button";
import contractAddress from "../chain-info/deployments/map.json";
import tokencontractABI from "../chain-info/contracts/GovernanceToken.json";
export const ReactFunctionChatVoiceBC = () => {
  const [history, setHistory] = useState([]);
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);
  const [isListening, setIsListening] = useState(false);
  const chatBoxRef = useRef(null);
  const [recipientAddress, setRecipientAddress] = useState("");
  const [amountInEther, setAmountInEther] = useState("");
  const [amounttoken, setAmounttoken] = useState("");
  const [functionName, setFunctionName] = useState("");
  const sendEther = async () => {
    if (window.ethereum) {
      try {
        await window.ethereum.request({ method: "eth_requestAccounts" });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Create a transaction object
        const tx = {
          to: recipientAddress,
          value: ethers.utils.parseEther(amountInEther),
        };
        setRecipientAddress("");
        setAmountInEther("");

        // Send the transaction
        const txResponse = await signer.sendTransaction(tx);

        // Wait for the transaction to be mined
        await txResponse.wait();

        alert("Transaction successful!");
      } catch (error) {
        console.error(error);

        alert("Transaction failed!");
      }
    } else {
      alert("Please install MetaMask!");
    }
  };
  const tokencontract_address = "0xd0bcD44A1f11E96C06aBF08f973A775e1c09FecE";
  const contract = contractAddress["11155111"]["GovernanceToken"][0];
  const tokenContractABI = tokencontractABI.abi;

  const SendTokens = async () => {
    if (window.ethereum) {
      try {
        await window.ethereum.request({ method: "eth_requestAccounts" });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const tokenContract = new ethers.Contract(
          tokencontract_address,
          tokenContractABI,
          signer
        );
        const tokencontractinstance = new ethers.Contract(
          contract,
          tokenContractABI,
          signer
        );

        const txResponse = await tokenContract.sendTokens(
          recipientAddress,
          amounttoken
        );

        await txResponse.wait();

        alert("Tokens sent successfully!");
        setRecipientAddress("");
        setAmountInEther("");
      } catch (error) {
        console.error(error);
        alert("Transaction failed!");
      }
    } else {
      alert("Please install MetaMask!");
    }
  };
  const handleRefresh = () => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://localhost:3500/getsendethdata"
        );
        setRecipientAddress(response.data.recipientAddress);
        setAmountInEther(response.data.amountInEther);
        setFunctionName(response.data.functionName);

        const response2 = await axios.get(
          "http://localhost:3500/getsendtokendata"
        );
        setRecipientAddress(response2.data.recipientAddress);
        setAmounttoken(response2.data.amounttoken);
        setFunctionName(response2.data.functionName);
      } catch (error) {
        console.error("Error fetching transaction data:", error);
      }
    };

    fetchData();
    if (functionName == "send_eth") {
      sendEther();
    }
    if (functionName == "send_token") {
      SendTokens();
    }
  };
  ///////////////////////////////////////

  useEffect(() => {
    chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
  }, [history]);

  // Initialize speech recognition
  const recognition = useRef(null);

  useEffect(() => {
    if (window.SpeechRecognition || window.webkitSpeechRecognition) {
      recognition.current = window.SpeechRecognition
        ? new window.SpeechRecognition()
        : new window.webkitSpeechRecognition();

      recognition.current.continuous = false;
      recognition.current.interimResults = false;
      recognition.current.lang = "en-US";

      recognition.current.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        console.log("Recognized text:", transcript); // Debugging output
        setPrompt(transcript); // Update state with recognized text
        sendPrompt(transcript); // Pass the recognized text directly to sendPrompt
      };

      recognition.current.onerror = (event) => {
        console.error("Speech recognition error:", event.error);
        setIsListening(false);
      };

      recognition.current.onend = () => {
        setIsListening(false);
      };
    } else {
      console.warn("Speech recognition not supported in this browser.");
    }
  }, []);

  const sendPrompt = async (text) => {
    setLoading(true);
    const userMessage = { prompt: text, type: "user", timestamp: Date.now() };
    setHistory((prevHistory) => [...prevHistory, userMessage]);

    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ input: text }),
    };

    try {
      const response = await fetch(
        "http://localhost:4321/process_input",
        requestOptions
      );

      const serverResponse = await response.text();
      const aiMessage = {
        prompt: serverResponse,
        type: "server",
        timestamp: Date.now(),
      };
      setHistory((prevHistory) => [...prevHistory, aiMessage]);
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      document.getElementById("sendButton").click();
    }
  };

  const startListening = () => {
    if (recognition.current) {
      setIsListening(true);
      recognition.current.start();
    }
  };

  const stopListening = () => {
    if (recognition.current) {
      recognition.current.stop();
    }
  };

  return (
    <div>
      <Box
        boxShadow={3}
        bgcolor="background.paper"
        p={2}
        className="retro-box"
        maxWidth="1000px"
        margin="auto"
        display="flex"
        flexDirection="column"
        alignItems="center"
      >
        <div className="App">
          <Box
            boxShadow={3}
            bgcolor="background.paper"
            p={2}
            className="retro-box"
            maxWidth="1000px"
            margin="auto"
            display="flex"
            flexDirection="column"
            alignItems="center"
          >
            <p>Conversational AI Assistant </p>
            <div ref={chatBoxRef} className="chat-box">
              <div className="history">
                {history.map((item, index) => (
                  <div key={index} className={`message ${item.type}`}>
                    {item.type === "user" ? "🧑🏻‍💻👩‍💻:" : "🤖:"} {item.prompt}
                  </div>
                ))}
              </div>
            </div>
          </Box>
          <div>
            <textarea
              className="textarea"
              placeholder="How can I help you"
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              onKeyPress={handleKeyPress}
            ></textarea>
          </div>
          <div className="send-button-container">
            <button
              id="sendButton"
              className={`send-button ${loading ? "disabled" : ""}`}
              disabled={loading}
              onClick={() => {
                if (prompt.trim()) {
                  sendPrompt(prompt);
                }
              }}
            >
              Send
            </button>
            <AwesomeButton
              type="whatsapp"
              className={`record-button ${isListening ? "listening" : ""}`}
              onPress={() => {
                if (isListening) {
                  stopListening();
                } else {
                  startListening();
                }
              }}
            >
              {isListening ? "Stop Recording" : "Voice chat"}
            </AwesomeButton>
            <AwesomeButton type="danger" onPress={handleRefresh}>
              Sign Transaction
            </AwesomeButton>
          </div>
        </div>
      </Box>
    </div>
  );
};
