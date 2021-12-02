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
    with open(Path('./contracts/compiled/certificate_abi.json')) as f:
        certificate_abi = json.load(f)

        # Setting the Smart Contract Address
        contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

        # Get