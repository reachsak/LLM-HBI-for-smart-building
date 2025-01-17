# Build your own DAO from Scratch, Smart Contracts, Moralis API with Backend and Complete Frontend.

## Preparation

Go to the frontend folder and install the dependencies with yarn

```shell
    yarn
```

change the `.env.example` on the main directory and add your private keys for:

- Wallet Private Key.
- Infura Project ID.
- Etherscan API key.

On the Backend folder inside "tokens" change the `.env.example` and add your Moralis Private key.

Install the python dependencies for the env:

- eth-brownie
- django
- web3

## Usage

Run the backend with python with.

````

Run the frontend with npm.

```shell
    npm start
````

## add llamafile server

launch terminal
cd llamafileold

llava7b
./llamafile-server-0.2.1 -m weight/llava-v1.5-7b-f16.gguf --mmproj weight/llava-v1.5-7b-mmproj-f16.gguf

llama213b
./llamafile-server-0.2.1 -m weight/llama-2-13b-chat.Q8_0.gguf

sharegpt4v13b
./llamafile-server-0.2.1 -m weight/ggml-model-Q4_K.gguf --mmproj weight/mmproj-model-f162.gguf

llava13b

Function calling model Berkeley
./llamafile-server-0.2.1 -m weight/gorilla-openfunctions-v2-q6_K.gguf

Function calling model Herme
./llamafile-server-0.2.1 -m weight/Hermes-2-Pro-Mistral-7B.Q8_0.gguf

Function calling natural function
./llamafile-server-0.2.1 -m weight/natural-functions.Q8_0.gguf

## run python server

cd backend
python3 server.py
python3 servertext.py

## run server js frontend

cd frontend
cd src
cd components
node serverllava.js
node serverllavatext.js
