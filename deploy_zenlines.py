
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv("test.env")

def deploy():
    minter_address = os.getenv("MINTER_ADDRESS")
    zenlines = zen_lines_nft.deploy(
        "ZenLinesToken", "ZRT",
        {"from":minter_address},
    )
    return zenlines
    
