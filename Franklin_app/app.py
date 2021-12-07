import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

from zen_lines_nft import createZenLines, setTokenURI

from pinata import convert_data_to_json, pin_file_to_ipfs, pin_json_to_ipfs    # These functions should appear on the pinata file



load_dotenv()

# Define and connect the Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Load contract using cache
@st.cache(allow_output_mutation=True)

# Load_contract function defined
def load_contract():
    # Load ABI
    with open(Path('./contracts/compiled/ZenLinesRegistry_abi.json')) as f:     # ABI JSON file for the ZenLinesRegistry contract
        ZenLinesRegistry_abi = json.load(f)

    # Setting the Smart Contract Address
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=certificate_abi
    )
    
    # Return the contract 
    return contract

# Load the contract
contract = load_contract()


# Uploading the files using Pinata and json


def pin_artwork(artwork_name, artwork_file):
    # Pin the file to IPFS with Pinata
    ipfs_file_hash = pin_file_to_ipfs(artwork_file.getvalue())  # This information comes from our pinata.py file

    # Build a token metadata file for the artwork
    token_json = {
        "name": artwork_name,
        "image": ipfs_file_hash
    }
    json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
    json_ipfs_hash = pin_json_to_ipfs(json_data)

    return json_ipfs_hash