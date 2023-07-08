import csv
import requests
from requests.auth import HTTPBasicAuth


# Covalent API
chainName = "eth-mainnet"
blockHeight = "latest"

apiEndPoint = "https://api.covalenthq.com/v1/eth-mainnet/block/latest/transactions_v3/"

# API Key
apiKey = HTTPBasicAuth('cqt_rQHDkTvfxm7dKCmqTfBmHfWTkVb8', '')

# Header
headers = {
    "accept": "application/json",
}


# Latest Block Fucntion
def getLatestBlock():
    response = requests.get(apiEndPoint, headers=headers, auth=apiKey)

    if response.status_code == 200:
        data = response.json()
        block = data["data"]["items"]
        return block

# write to CSV
def writeTransactionToCSV(latestBlock):
    csvFile = "transactionLatestBlock.csv"
    with open(csvFile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Transaction To", "Transaction From", "Amount"])

        for tx in latestBlock:
            writer.writerow([tx["to_address"], tx["from_address"], tx["value"]])

latestBlock = getLatestBlock()
if latestBlock:
    print("block number: ",latestBlock[0]["block_height"])
    print("block timestamp: ",latestBlock[0]["block_signed_at"])
    for item in latestBlock:
        print("transaction to: ", item["to_address"])
        print("transaction from:", item["from_address"])
        print("amount: ", item["value"])
else:
    print("error 400")

writeTransactionToCSV(latestBlock=latestBlock)

    