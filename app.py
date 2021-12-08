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
    with open(Path('./contracts/compiled/gallery_abi.json')) as f:     # ABI JSON file for the Zen_Lines Gallery contract
        gallery_abi = json.load(f)
    
    # Setting the Smart Contract Address
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=gallery_abi
    )
    
    # Return the contract 
    return contract

# Load the contract
contract = load_contract()


st.markdown("## ZEN LINES MUSIC AND IMAGE NFT")


st.title("Music and Image Registry in our Gallery and Appraisal System")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

################################################################################
# Register New Musical Creation
################################################################################
st.markdown("## Register Music and Image NFT in our Gallery")

name = st.text_input("Enter the name of the musical creation")
artist = st.text_input("Enter the artist name")
initialValue = st.text_input("Enter the initial appraisal amount")
tokenURI = st.text_input("Enter the URI to the musical creation")

if st.button("Register Musical Creation"):
    tx_hash = contract.functions.artworkRegistration(
        address,
        name,
        artist,
        int(initialValue),
        tokenURI
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
st.markdown("---")


################################################################################
# Appraise Musical Creation
################################################################################
st.markdown("## Appraise Musical Creation")
tokens = contract.functions.totalSupply().call()
tokenId = st.selectbox("Choose a Token ID", list(range(tokens)))
newValue = st.text_input("Enter the new appraisal amount")
reportURI = st.text_area("Enter notes about the appraisal")
if st.button("Appraise Musical Creation"):

    # Use the tokenId and the reportURI to record the appraisal
    tx_hash = contract.functions.newArtwork(
        tokenId,
        int(newValue),
        reportURI
    ).transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write(receipt)
st.markdown("---")

################################################################################
# Get Appraisals
################################################################################
st.markdown("## Get the appraisal report history")
art_token_id = st.number_input("Artwork ID", value=0, step=1)
if st.button("Get Appraisal Reports"):
    appraisal_filter = contract.events.Appraisal.createFilter(
        fromBlock=0,
        argument_filters={"tokenId": art_token_id}
    )
    appraisals = appraisal_filter.get_all_entries()
    if appraisals:
        for appraisal in appraisals:
            report_dictionary = dict(appraisal)
            st.markdown("### Appraisal Report Event Log")
            st.write(report_dictionary)
            st.markdown("### Appraisal Report Details")
            st.write(report_dictionary["args"])
    else:
        st.write("This artwork has no new appraisals")
