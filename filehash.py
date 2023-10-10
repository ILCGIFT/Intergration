import hashlib
from web3 import Web3

# Read data from CSV/EXCEL/TXT file
with open('data1.csv/xlsx/txt', 'rb') as file:
    csv_data = file.read()
    
# Calculate hash of data
hash_value = hashlib.sha256(csv_data).hexdigest()

# Connect to the ILC network
w3 = Web3(Web3.HTTPProvider('YOUR_ILC_NODE_URL'))

# Address of the smart contract
contract_address = '0xYourContractAddress'
contract_abi = [...] # ABI of the smart contract

# Connect to smart contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Store hash on blockchain
contract.functions.storeHash(hash_value).transact({'from': w3.eth.defaultAccount})

print("Hash stored on blockchain:", hash_value)
