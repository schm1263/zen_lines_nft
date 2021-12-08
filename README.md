
# zen_lines_nft

### For our project we decided to write smart contracts for an NFT. I provided the artwork, a hand drawn icon, and music, created by my co-producer and I, for the NFT.
#### Example here:

https://user-images.githubusercontent.com/85138335/145272947-fd33a3bf-6dec-484d-901e-40adc40d3166.mp4

### I uploaded the file using IPFS Desktop, though the IPFS CLI could also achieve the same result. We used the URI from IPFS and input it into some aspects of the smart contracts, as well as the streamlit app itself.

### I then wrote a smart contract that would function like a gallery, meant to hold the NFT as well as any future NFT drop.

### Once combined with the other smart contracts and the streamlit code, we now had a functioning streamlit app connected to a smart contract that serves as a gallery.

### In short it allows for a user to input a wallet address and a token URI to store the artwork in the gallery and even get appraisal information.
=======
# Zen Lines NFT Project

## For this project our goal was to create an NFT of Cole's zen lines artwork and music. The first step was to create the NFT contract and deploy it to a test network.

## We wrote and compiled the contract using OpenZepplin libraries for ERC721, Ownable, and Counters. ERC721 is the token standard for NFTs. The ownable access restrictor provides security to the contract by implementing standard ownership coding practices. Counters is a utility library for simplifying token ID generation, it uses less computational effort and therefore less gas. In order to use Counters.sol utility function for token IDs and the Ownable.sol access restrictor we had to use pragma solidity 0.8.0. Using pragma 0.8.0 required us to import the ERC721URIStorage extension in order to make use of the built in _setTokenURI function as it was moved from the ERC721.sol when pragma 0.8.0 was released.

## Compiled NFT contract:
![Image](./screen_shots/compiled_nft_contract.png)

## Once the contract was able to be compiled we deployed the contract to the Rinkeby test network. It can be found on Etherscan here: https://rinkeby.etherscan.io/tx/0xf13444561246587110c2b9ca48a9ff57a76dbfbb6da8640b461f90472e7be2f3

## Looking at the deployed contract in Remix IDE we see that we can call the "createZenLines" function, and input owner address and tokenURI to make an NFT with token ID 1 and a tokenURI that points to our metadata on IPFS https://user-images.githubusercontent.com/85138335/145272947-fd33a3bf-6dec-484d-901e-40adc40d3166.mp4 

## NFT creation example on Remix:
![Image](./screen_shots/createZenLines_1.png)

## Using this contract address and the ABI file in JSON format the next steps were to create metadata on IPFS for the NFT, create a UI using streamlit to create Zen Lines NFTs by generating token URIs attached to token IDs that point to our artwork stored in IPFS, and create an auction contract for selling the NFTs.

