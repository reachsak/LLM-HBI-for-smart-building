import React, { useEffect, useState, useRef } from "react";
import Box from "@mui/material/Box";
import "./Display.css";

export const ReactFunctionchat = () => {
  const [history, setHistory] = useState([]);
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);
  const chatBoxRef = useRef(null);

  const sendPrompt = async () => {
    setLoading(true);
    const userMessage = { prompt, type: "user", timestamp: Date.now() };
    setHistory((prevHistory) => [...prevHistory, userMessage]);

    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ input: prompt }),
    };

    try {
      const response = await fetch(
        "http://localhost:4321/process_input",
        requestOptions
      );

      // Log the response for debugging
      console.log("Response status:", response.status);
      console.log("Response headers:", response.headers);

      // Handle response as text since the server returns HTML
      const text = await response.text();
      console.log("Response text:", text);

      // Create an AI message from the response text
      const aiMessage = { prompt: text, type: "server", timestamp: Date.now() };
      setHistory((prevHistory) => [...prevHistory, aiMessage]);
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
  }, [history]);

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      document.getElementById("sendButton").click();
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
            <p>Conversational AI Agent</p>
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
                setPrompt("");
                sendPrompt();
              }}
            >
              Send
            </button>
          </div>
        </div>
      </Box>
    </div>
  );
};
