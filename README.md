# Zen Lines NFT Project

## My role in this project was to create the NFT contract and deploy it.

## I was able to write and compile the contract using OpenZepplin libraries for ERC721, Ownable, and Counters. In order to use Counters.sol utility function for token IDs and the Ownable.sol access restrictor I had to use pragma solidity 0.8.0. Using pragma 0.8.0 requires me to import the ERC721URIStorage extension in order to make use of the built in _setTokenURI function as it was moved from the ERC721.sol when pragma 0.8.0 was released.

## Compiled NFT contract screeshot:
![Image](./screen_shots/compiled_nft_contract.png)

## Once the contract was able to be compiled I deployed the contract to the Rinkeby test network. It can be found on Etherscan here: https://rinkeby.etherscan.io/tx/0xf13444561246587110c2b9ca48a9ff57a76dbfbb6da8640b461f90472e7be2f3

## Using this contract address and the ABI file in JSON format we can create a UI using streamlit to create Zen Lines NFTs generating token URIs that point to our artwork stored in IPFS.