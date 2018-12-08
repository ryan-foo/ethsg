# KyberCharts

![Kyber Logo](https://kyber.network/media/logos/kyber-logo.png)

## Description

KyberCharts aims to provide historical data for tokens traded on the Kyber Network. This takes the form of a Python library.

The function would take in a start block and an end block, and return a pandas dataframe containing all of Kyber's transactions on the main.net of Ethereum Blockchain in the form OHLCV (Open, High, Low, Closing, Volume).

The use cases range from analytics, to bot trading, to the simple [love of data](https://reddit.com/r/dataisbeautiful).

The tool queries the smart contracts associated with the Kyber Network and searches through the blocks for the transaction history.

The function can be adjusted to query a range of dates of historical trading data and subsequently visualise it. For example, as a developer, you could use our library to query for the past month of transactions from ETH to ZIL with this API.

We also have implemented a front-end demo with a visualization as a proof of concept.

```

```

## Installation

```bash
git clone https://github.com/ryan-foo/ethsg.git
```

Run this command in your terminal.

```
python3 blahblah.py
```

The program will query data from the Ethereum mainnet and automatically cleans it to OHLCV (Open, High, Low, Closing, Volume) data and stores it as a .csv. Beware -- the Ethereum mainnet is a very large set of data to get through!

## Comments / The Process

We had to decide between using the etherscan API and reading directly off the blockchain or through Infura.

We aimed to create an API.

Based on our team's competencies, we decided between Python and Web3js as a means of getting the historical data from either etherscan. We saved this in a Jupyter Notebook. The end-goal was a Python library because the end goal was a data-science library.

We accessed the main-net.

Due to the constraints of the hackathon. Our webapp was also limited in its front-end and user experience. However, we believe the main target audience are developers and algorithmic traders, who will find the clean .csv useful for their purposes.



## Technicals

## Stretch Goals

One of our stretch goals was to improve the user experience by reading the public key of the user and displays to them the tokens most relevant to them.

## Credits (in alphabetical order)

Anthony Cheung, Jeffery Cao, Ryan Foo, Yash Sinha