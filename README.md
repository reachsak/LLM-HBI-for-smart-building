# Large Language Model for Human-Building Interaction

## Manuscript
[Autonomous Building Cyber-Physical Systems Using Decentralized Autonomous Organizations, Digital Twins, and Large Language Model](https://arxiv.org/abs/2410.19262)
## Project Overview
The Project aims to facilitate the human-building interaction within smart building using open sourced LLM such as LLaMA 3. This AI assistant aims to provide smart and personalized assistance to occupants through web app. Users can communicate with the AI virtual assistant through text and voice input to control various building facilities, adjust setpoints for the specific building smart facilities, or turn systems on or off as needed. The assistant also provides real-time information on indoor environmental conditions by accessing live sensor data reading from the IoT device. The Text-to-Speech (TTS) and Speech-to-Text (STT) models are powered by open sourced tool and models such as Whisper and Piper.

<img src="/fig2.png" style="float: left; margin-right: 20px; max-width: 200px;">

## Video Demo
[![Watch the demo video](https://img.youtube.com/vi/0SyZHvmadZA/0.jpg)](https://www.youtube.com/watch?v=0SyZHvmadZA)  
*Click on the image to view the demo video.*

## Summary
<img src="/fig1.png" style="float: left; margin-right: 20px; max-width: 200px;">
<img src="/equipment.png" style="float: left; margin-right: 20px; max-width: 200px;">




### Key Features

- **Large Language Model-Based Chatbot:** Enables natural language interactions with building management systems.
- **Smart Facilities Control:** Integrates with smart building systems to provide efficient control and management through conversational interfaces.
- **Open-Source TTS and STT Models:** Utilizes open-source Text-to-Speech and Speech-to-Text models for seamless voice communication.


## Run

./llamafile-server-0.2.1 -m weight/Meta-Llama-3-8B-Instruct.Q8_0.gguf

### Requirements

- Python 3.10
- Open-source Text-to-Speech (TTS) model
- Open-source Speech-to-Text (STT) model
- Open-source Large language model (e.g., LLaMA)


