import requests
def fund_account(address):
    r = requests.get('https://horizon-testnet.stellar.org/friendbot?addr=' + address)
    return r.text

if __name__ == '__main__':
   
    print("For Issuer Addres")
    ISSUER_ADDRESS="Put-Your-Issuer-Public-Key-Here"
    result = fund_account(ISSUER_ADDRESS)
    print(result)

    print("For Reciver Addres")
    RECIVER_ADDRESS="Put-Your-Reciver-Public-Key-Here"
    result = fund_account(RECIVER_ADDRESS)
    print(result)
  