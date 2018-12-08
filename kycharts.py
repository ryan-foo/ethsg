
# coding: utf-8

# In[1]:


import requests
import json


# In[31]:


url = "https://mainnet.infura.io/v3/9e0815b80e6f49d6af72229dfa69a926"
headers = {'content-type': 'application/json'}

    # Example echo method
payload = {
"method": "eth_getLogs",
"params": [{"fromBlock":"0x5A3394", "toBlock": "0x5A33AD"}],
"jsonrpc": "2.0",
"id": 1,
}
response = requests.post(url, data=json.dumps(payload), headers=headers).json()


# In[32]:


len(response['result'])


# In[33]:


response


# In[34]:


##starting with oldest address, batch transactions into smaller intervals and stitch together 
##filter out all but KyberTrade/Execute Trade transactions 
##ExecuteTrade topic = 0x1849bd6a030a1bca28b83437fd3de96f3d27a5d172fa7e9c78e7b61468928a39
##KyberTrade topic = 0x1c8399ecc5c956b9cb18c820248b10b634cca4af308755e07cd467655e8ec3c7


# In[52]:


def decToHex(block_number):
    return hex(block_number)


# In[43]:


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


# In[44]:


getCurrentBlock()


# In[47]:


def hexToDec(block_number):
    return int(block_number, 16)


# In[48]:


hexToDec(getCurrentBlock())


# In[86]:


def getHistoricalEvents(start_block, end_block):
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
    print(len(response['result']))
    return response['result']


# In[87]:


start = 5911444
one = getHistoricalEvents(start,start+10)


# In[88]:


one


# In[89]:


from web3 import Web3


# In[90]:


#
#event KyberTrade(address srcAddress, ERC20 srcToken, uint srcAmount, address destAddress, ERC20 destToken, uint destAmount);


# In[93]:


def isTrade(event):
    


# In[155]:


someTrades = getHistoricalEvents(hexToDec(getCurrentBlock())-50,hexToDec(getCurrentBlock()))


# In[152]:


someTrades


# In[110]:


len(someTrades[0]['data'])


# In[111]:


someTrades[0]['data']


# In[237]:


import numpy as np
import pandas as pd


# In[113]:


len('0x000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee00000000000000000000000023ccc43365d9dd3882eab88f43d515208f832430000000000000000000000000000000000000000000000000008e1bc9bf040000000000000000000000000000000000000000000000000021bc77e9f9a3790342')


# In[240]:


numTrades = 0
trades = np.ndarray(len(someTrades))
blocks = np.ndarray(len(someTrades))
for event in someTrades:
    dummy = decode_hex(event['data'])
    if (len(dummy) > 100 and event['address'] == '0x91a502c678605fbce581eae053319747482276b9'):
        print(numTrades)
        print(event)
        print(event['address'])
        print("\n")
        print(dummy)
        test = decode_abi(['address', 'address', 'uint256', 'address', 'address', 'uint256'], dummy)
        print("\n")
        print(test)
        trades[numTrades] = test
        blocks[numTrades] = event['blockNumber']
        print("\n")
        numTrades += 1
print("Number of trades:", numTrades)


# In[116]:


from eth_abi import decode_single, decode_abi


# In[117]:


#if length of data is 258, then assume it is a KyberTrade and decode accordingly 
#address srcAddress, ERC20 srcToken, uint srcAmount, address destAddress, ERC20 destToken, uint destAmount


# In[129]:


someTrades


# In[148]:


#decode_abi(['bytes1', 'bytes1', 'int', 'bytes1', 'bytes1', 'int'], b'a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
for event in someTrades:
    data = bytes(event['data'], 'raw_unicode_escape')
    print(len(data))
    #decode_abi(['bytes1', 'bytes1', 'int', 'bytes1', 'bytes1', 'int'], data)


# In[159]:


test = '0x0000000000000000000000000f5d2fb29fb7d3cfee444a200298f468908cc94200000000000000000000000000000000000000000000005b549ccb3d5d719e08000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee0000000000000000000000000000000000000000000000000ee0fe1a67519c4100000000000000000000000091a502c678605fbce581eae053319747482276b9'


# In[141]:


#encode(test, 'raw_unicode_escape')
from codecs import encode


# In[160]:


encode(test, 'raw_unicode_escape')


# In[189]:


decode_abi(['address', 'address', 'uint256', 'address', 'address', 'uint256'], b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x85\xc5\xc2m\xc2\xafUF4\x1f\xc1\x98\x8b\x9d\x17\x81H\xb4\x83\x8b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f]/\xb2\x9f\xb7\xd3\xcf\xeeDJ \x02\x98\xf4h\x90\x8c\xc9B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00T\xdc\xcd\xbe\rX\xe1R\xcc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x85\xc5\xc2m\xc2\xafUF4\x1f\xc1\x98\x8b\x9d\x17\x81H\xb4\x83\x8b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\xcb\xce\xef#\x97\x15y')


# In[190]:


issabyte = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x85\xc5\xc2m\xc2\xafUF4\x1f\xc1\x98\x8b\x9d\x17\x81H\xb4\x83\x8b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f]/\xb2\x9f\xb7\xd3\xcf\xeeDJ \x02\x98\xf4h\x90\x8c\xc9B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00T\xdc\xcd\xbe\rX\xe1R\xcc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x85\xc5\xc2m\xc2\xafUF4\x1f\xc1\x98\x8b\x9d\x17\x81H\xb4\x83\x8b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\xee\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\xcb\xce\xef#\x97\x15y'


# In[191]:


len(issabyte)


# In[173]:


s = '0x0000000000000000000000000f5d2fb29fb7d3cfee444a200298f468908cc94200000000000000000000000000000000000000000000005b549ccb3d5d719e08000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee0000000000000000000000000000000000000000000000000ee0fe1a67519c4100000000000000000000000091a502c678605fbce581eae053319747482276b9'
b = bytearray()
b.extend(map(ord, s))


# In[178]:


from eth_utils import decode_hex
decoded = decode_hex(s)


# In[184]:


decoded


# In[198]:


def decodeTrade(rawData):
    decode_abi(['address', 'address', 'uint256', 'address', 'address', 'uint256'], rawData)


# In[233]:


def getRawTrades(num_blocks):
    eventsBatch = getHistoricalEvents(hexToDec(getCurrentBlock())-50,hexToDec(getCurrentBlock()))
    numTrades = 0
    for event in eventsBatch:
        dummy = decode_hex(event['data'])
        if (len(dummy) > 100 and event['address'] == '0x91a502c678605fbce581eae053319747482276b9'):
            numTrades += 1
            print(numTrades)
            #print(event)
            print(event['address'])
            print("\n")
            print(dummy)
            test = decode_abi(['address', 'address', 'uint256', 'address', 'address', 'uint256'], dummy)
            print("\n")
            print(test)
            print("\n")
        
    print("Number of trades:", numTrades)
    


# In[241]:


5911444


# In[243]:


hexToDec(getCurrentBlock())


# In[246]:


(6850615 - 5911444)/50


# In[ ]:


start = 5911444
end = 6850615
z = 0
tradeData = pd.DataFrame()
while(start+50*(z+1) < end):
    eventsBatch = getHistoricalEvents(start + z*50, start+50*(z+1))
    for event in eventsBatch:
        dummy = decode_hex(event['data'])
        if (len(dummy) == 192 and event['address'] == '0x91a502c678605fbce581eae053319747482276b9'):
            numTrades += 1
            test = decode_abi(['address', 'address', 'uint256', 'address', 'address', 'uint256'], dummy)
            block_num = event['blockNumber']
            tradeData['block'] = block_num
            tradeData['rawdata'] = test
            print(z)
            
    z += 1       

