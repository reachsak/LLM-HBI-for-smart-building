import React, { useState } from "react";
import { Box, Button } from "@mui/material";
import "react-awesome-button/dist/styles.css";
import {
  AwesomeButton,
  AwesomeButtonProgress,
  AwesomeButtonSocial,
} from "react-awesome-button";

const WebPagedigitaltwin = () => {
  const [showWebPage, setShowWebPage] = useState(false);
  const [marginLeft, setMarginLeft] = useState(0);

  const handleButtonClick = () => {
    setShowWebPage(true);
  };

  return (
    <div
      style={{
        position: "relative",
        overflow: "hidden",
        margin: -100,
        padding: 0,
      }}
    >
      <iframe
        src="http://localhost:9000/"
        style={{
          border: "none",
          width: "100%",
          height: "1000px",
          marginLeft: `${marginLeft}px`,
        }}
        title="Web Page"
      ></iframe>
    </div>
  );
};

export default WebPagedigitaltwin;
