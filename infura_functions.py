
# coding: utf-8

# In[5]:


##Trade History Scraping 
import requests
import json
from eth_utils import decode_hex

def getCurrentBlock():
    url = "https://mainnet.infura.io/v3/9e0815b80e6f49d6af72229dfa69a926"
    headers = {'content-type': 'application/json'}

        # Example echo method
    payload = {
    "method": "eth_blockNumber",
    "params": [{}],
    "jsonrpc": "2.0",
    "id": 1,
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    return response['result']


# In[4]:


def decToHex(block_number):
    return hex(block_number)

def hexToDec(block_number):
    return int(block_number, 16)

def getPastEvents(start_block, end_block):
    url = "https://mainnet.infura.io/v3/9e0815b80e6f49d6af72229dfa69a926"
    headers = {'content-type': 'application/json'}
    fromBlock = str(decToHex(start_block))
    toBlock = str(decToHex(end_block))
    print(fromBlock)
    print(toBlock)
    payload = {
    "method": "eth_getLogs",
    "params": [{"fromBlock":fromBlock, "toBlock": toBlock}],
    "jsonrpc": "2.0",
    "id": 1,
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    return response['result']


# In[6]:


def getRawTrades(start_block, end_block):
    trades = {}
    eventsBatch = getPastEvents(start_block, end_block)
    numTrades = 0
    for event in eventsBatch:
        data = decode_hex(event['data'])
        if (len(data) == 192 and event['address'] == '0x91a502c678605fbce581eae053319747482276b9'):
            
            event_data = decode_abi(['address', 'address', 'uint256', 'address', 'address', 'uint256'], dummy)
            trade_data = event_data + (hexToDec(event['blockNumber']),)
            trades[numTrades] = trade_data
            numTrades += 1
        
    print("Number of trades:", numTrades)
    return trades
    

