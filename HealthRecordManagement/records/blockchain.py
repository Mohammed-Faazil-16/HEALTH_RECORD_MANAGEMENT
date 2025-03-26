from web3 import Web3
import json

# Connect to Ganache (or Ethereum Testnet later)
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Replace with your contract address and ABI (from Truffle/Ganache)
contract_address = "0xc4404cc41ac5Ede48e0CF53199D7CbCEC7BfFDA9"  # After deploying with Truffle
with open("C:/ghidorah/Health_Record_Management/build/contracts/HealthRecords.json") as f:  # ABI from Truffle build
    contract_data = json.load(f)
    abi = contract_data["abi"]

contract = web3.eth.contract(address=contract_address, abi=abi)

def add_record(patient_id, doctor_id, diagnosis, prescription, record_hash, sender_address):
    account = web3.eth.accounts[0]  # Use Ganache’s first account for now
    tx_hash = contract.functions.addRecord(
        patient_id, doctor_id, diagnosis, prescription, record_hash
    ).transact({"from": sender_address})
    return tx_hash.hex()

def get_records(patient_address):
    records = contract.functions.getMyRecords().call({"from": patient_address})
    return records