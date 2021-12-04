pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/Counters.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";

// Create an NFT contract that inherits the Ownable.sol property from open zepplin
contract ZenLinesToken is Ownable, ERC721Full {
    
    // use counters.sol to set token IDs
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    
     // create a constructor to set token name and symbol
     constructor() public ERC721Full("ZenLinesToken", "ZRT") {}

    // create a function to generate the NFT
    function createZenLines(address owner, string memory tokenURI) public returns (uint256) {
        // increment the token id
        _tokenIds.increment();
        
        // create a uint variable for the new NFT ID and set it equal to the current increment
        uint256 tokenId = _tokenIds.current();
        // mint the new NFT with the owner address and ID
        _mint(owner, newTokenId);
        // set the token URI for this NFT
        _setTokenURI(newTokenId, tokenURI);
        // return the token ID
        return newTokenId;
    }
    // Create function to set token URI
    function setTokenURI(unint256 tokenId, string memory _tokenURI) public {
        // create require statement so that only the token owner can set the token URI 
        require(
            _isApprovedOrOwner(_msg.sender(), tokenId), "You are not the owner!");
            _setTokenURI(tokenId, _tokenURI);

    }
}