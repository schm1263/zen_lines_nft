import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contract/access/Ownable.sol";

// Create an NFT contract that inherits the Ownable.sol property from open zepplin
contract ZenLines is Ownable, ERC721 {
    // use counters.sol to set token IDs
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    using Strings for uint256;
    
}