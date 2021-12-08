pragma solidity ^0.8.0;
// in order to use Counters.sol utility function for token IDs and the Ownable.sol access restrictor I have to use pragma solidity 0.8.0
// using pragma 0.8.0 requires me to import the ERC721URIStorage extension in order to make use of the built in _setTokenURI function as it was moved from the ERC721.sol when pragma 0.8.0 was released
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/Counters.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";

// Create an NFT contract that inherits the Ownable.sol property from open zepplin
contract ZenLinesToken is Ownable, ERC721URIStorage {
    
    // use counters.sol to set token IDs
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    
     // create a constructor to set token name and symbol
     constructor() ERC721("ZenLinesToken", "ZRT") {}

    // create a function to generate the NFT
    function createZenLines(address owner, string memory tokenURI) public returns (uint256) {
        // increment the token id
        _tokenIds.increment();
        // create a uint variable for the new NFT ID and set it equal to the current increment
        uint256 newTokenId = _tokenIds.current();
        // mint the new NFT with the owner address and ID
        _safeMint(owner, newTokenId);
        // set the token URI for this NFT
        _setTokenURI(newTokenId, tokenURI);
        // return the token ID
        return newTokenId;
    }
    
}