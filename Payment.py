from stellar_base.horizon import horizon_testnet
from stellar_base.operation import ChangeTrust,Payment
from stellar_base.transaction import Transaction
from stellar_base.memo import TextMemo
from stellar_base.asset import Asset
from stellar_base.keypair import Keypair
from stellar_base.transaction_envelope import TransactionEnvelope as Te
import time 

def transfer_fund(amount, asset_object, customer_account, issuer_account, issuer_seed):
    horizon = horizon_testnet()
    print('Transferring fund to {}'.format(customer_account))
    op = Payment(
        destination=customer_account, 
        asset=asset_object,
        amount=str(amount), 
        source=issuer_account
    )
    msg = TextMemo('Your first Payment !')
    sequence = horizon.account(issuer_account).get('sequence')
    tx = Transaction(
        source=issuer_account,
        sequence= sequence,
        memo= msg,
        fee=None,
        operations=[op],
    )
    issuer_account1 = Keypair.from_seed(issuer_seed)
    envelope = Te(tx=tx, signatures=None, network_id="TESTNET")
    
    envelope.sign(issuer_account1)
    xdr_envelope = envelope.xdr()
  
    response = horizon.submit(xdr_envelope)
    print(response)
    if 'result_xdr' in response:
        print('Successful Transfer')
    else:
        print('Things go Fishy')
if __name__ == '__main__':
    at=Asset(code='YourAssetCode', issuer='Put-Your-Issuer-Public-Key-Here')
    transfer_fund(10,at,
    'Put-Your-Reciver-Public-Key-Here',
    'Put-Your-Issuer-Public-Key-Here',
    'Put-Your-Issuer-Secret-Key-Here'
    )
