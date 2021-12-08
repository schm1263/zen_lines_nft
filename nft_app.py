import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
# Define and connect the Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
# Load contract using cache
@st.cache(allow_output_mutation=True)
# Load_contract function defined
def load_contract():
    # Load ABI
    with open(Path('./contracts/compiled/zen_lines_abi.json')) as f:     # ABI JSON file for the Zen_Lines NFT contract
       zen_lines_abi = json.load(f)
    # Setting the Smart Contract Address
    contract_address = os.getenv("NFT_SMART_CONTRACT_ADDRESS")
    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=zen_lines_abi
    )
    # Return the contract
    return contract
# Load the contract
contract = load_contract()
st.markdown("## ZEN LINES MUSIC AND IMAGE NFT")
st.title("Cole Mills Zen Lines NFT")
################################################################################
# Creation of a tokenID for an NFT - Music
################################################################################
st.markdown("## Token ID Creation for Music and Image NFT")
owner = st.text_input("Enter an address here:")
tokenURI = st.text_input("Enter the URI to the musical creation:")
if st.button("TokenID for Music and Image NFT"):
    tx_hash = contract.functions.createZenLines(
        owner,
        tokenURI
    ).transact({'from': owner, 'gas': 1000000})
    transaction = w3.eth.getTransaction(tx_hash)
    st.write("Transaction info:")
    st.write(contract.decode_function_input(transaction.input))
st.markdown("---")