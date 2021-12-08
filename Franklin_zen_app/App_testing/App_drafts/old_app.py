import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

from deploy_zenlines import deploy



# The deploy function comes from the deploy_zenlines file

load_dotenv()

# Define and connect the Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Load contract using cache
@st.cache(allow_output_mutation=True)

# Load_contract function defined
def load_contract():
    # Load ABI
    with open(Path('./contracts/compiled/gallery_abi.json')) as f:     # ABI JSON file for the Zen_Lines contract
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


#########################################
#   Displaying the File                #
#########################################

""" st.markdown("## ZEN LINES MUSIC AND IMAGE NFT")
 """




# Uploading the files using Pinata and json


""" def pin_artwork(artwork_name, artwork_file):
    # Pin the file to IPFS 
    ipfs_file_hash = pin_file_to_ipfs(artwork_file.getvalue())  # This information comes from our pinata.py file """

 """    # Build a token metadata file for the artwork
    token_json = {
        "name": artwork_name,
        "image": ipfs_file_hash
    }
    json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
    json_ipfs_hash = pin_json_to_ipfs(json_data)

    return json_ipfs_hash


st.title("Original Creations - Music NFT Purchasing System")
st.write("Choose an account to get started") 
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")


 """

# I don't think we need an appraisal report but information is here just in case



""" 
#def pin_appraisal_report(report_content):
#    json_report = convert_data_to_json(report_content)
#    report_ipfs_hash = pin_json_to_ipfs(json_report)
#    return report_ipfs_hash





################################################################################
# Register New Artwork
################################################################################
st.markdown("## Register New Artwork")
artwork_name = st.text_input("Enter the name of the artwork")
artist_name = st.text_input("Enter the artist name")
initial_appraisal_value = st.text_input("Enter the initial appraisal amount")

# Use the Streamlit `file_uploader` function create the list of digital image file types(jpg, jpeg, or png) that will be uploaded to Pinata.
file = st.file_uploader("Upload Artwork", type=["jpg", "jpeg", "png"])

if st.button("Register Artwork"):
    # Use the `pin_artwork` helper function to pin the file to IPFS
    artwork_ipfs_hash = pin_artwork(artwork_name, file)

    artwork_uri = f"ipfs://{artwork_ipfs_hash}"

    tx_hash = contract.functions.registerArtwork(
        address,
        artwork_name,
        artist_name,
        int(initial_appraisal_value),
        artwork_uri
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    st.write("You can view the pinned metadata file with the following IPFS Gateway Link")
    st.markdown(f"[Artwork IPFS Gateway Link](https://ipfs.io/ipfs/{artwork_ipfs_hash})")
st.markdown("---")






################################################################################
# Appraise Art
################################################################################
st.markdown("## Appraise Artwork")
tokens = contract.functions.totalSupply().call()
token_id = st.selectbox("Choose an Art Token ID", list(range(tokens)))
new_appraisal_value = st.text_input("Enter the new appraisal amount")
appraisal_report_content = st.text_area("Enter details for the Appraisal Report")

if st.button("Appraise Artwork"):

    # Use Pinata to pin an appraisal report for the report content
    appraisal_report_ipfs_hash =  pin_appraisal_report(appraisal_report_content)

    # Copy and save the URI to this report for later use as the smart contract’s `reportURI` parameter.
    report_uri = f"ipfs://{appraisal_report_ipfs_hash}"

    tx_hash = contract.functions.newAppraisal(
        token_id,
        int(new_appraisal_value),
        report_uri
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
        fromBlock=0, argument_filters={"tokenId": art_token_id}
    )
    reports = appraisal_filter.get_all_entries()
    if reports:
        for report in reports:
            report_dictionary = dict(report)
            st.markdown("### Appraisal Report Event Log")
            st.write(report_dictionary)
            st.markdown("### Pinata IPFS Report URI")
            report_uri = report_dictionary["args"]["reportURI"]
            report_ipfs_hash = report_uri[7:]
            st.markdown(
                f"The report is located at the following URI: "
                f"{report_uri}"
            )
            st.write("You can also view the report URI with the following ipfs gateway link")
            st.markdown(f"[IPFS Gateway Link](https://ipfs.io/ipfs/{report_ipfs_hash})")
            st.markdown("### Appraisal Event Details")
            st.write(report_dictionary["args"])
    else:
        st.write("This artwork has no new appraisals")


################################################################################
# Display a Token
################################################################################
st.markdown("## Display an Art Token")

selected_address = st.selectbox("Select Account", options=accounts)

tokens = contract.functions.balanceOf(selected_address).call()

st.write(f"This address owns {tokens} tokens")

token_id = st.selectbox("Artwork Tokens", list(range(tokens)))

if st.button("Display"):

    # Use the contract's `ownerOf` function to get the art token owner
    owner = contract.functions.ownerOf(token_id).call()

    st.write(f"The token is registered to {owner}")

    # Use the contract's `tokenURI` function to get the art token's URI
    token_uri = contract.functions.tokenURI(token_id).call()

    st.write(f"The tokenURI is {token_uri}")
    st.image(token_uri)


 """