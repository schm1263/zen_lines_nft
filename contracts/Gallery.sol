pragma solidity ^0.5.0;

//*Import ERC721 OpenZepplin Library
//*Create Tokens

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ZenLinesRegistery is ERC721Full {

    constructor() ERC721Full("ZenLineToken","ZRT") public {}

    struct ZenLines {
        string name;
        string artist;
        uint appraisedValue;
        //uint dateCreated;
        //string description;
    }

    mapping(uint => ZenLines) public gallery;

    event Appraisal(uint tokenId, uint appraisedValue, string reportURI);

    function artworkRegistration(address owner, string memory name, string memory artist, uint initialValue, string memory tokenURI) public returns(uint){
        uint tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        gallery[tokenId] = ZenLines(name, artist, initialValue);

        return tokenId;
    }

    function newArtwork(uint tokenId, uint newValue, string memory reportURI) public returns(uint) {
        gallery[tokenId].appraisedValue = newValue;

        emit Appraisal(tokenId, newValue, reportURI);

        return gallery[tokenId].appraisedValue;
    }
}