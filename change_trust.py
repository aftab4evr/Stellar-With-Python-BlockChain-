from stellar_base.horizon import horizon_testnet
from stellar_base.operation import ChangeTrust,Payment
from stellar_base.transaction import Transaction
from stellar_base.memo import TextMemo
from stellar_base.asset import Asset
from stellar_base.keypair import Keypair
from stellar_base.transaction_envelope import TransactionEnvelope as Te

def opr_change_trust(asset_object, receiver_address, receiver_seed):
    horizon = horizon_testnet()
    sequence = horizon.account(receiver_address).get('sequence')
    print(sequence)
    op = ChangeTrust(
        asset=asset_object,
        limit='5000',
        source=receiver_address
    )
    # print(op.__dict__)
    msg = TextMemo('Change Trust Operation')   
    receiving_account = Keypair.from_seed(receiver_seed)
    tx = Transaction(
        source=receiving_account.address().decode(),
        sequence=sequence,
        time_bounds=None,
        memo=msg,
        fee=None,
        operations=[op],
    )
    envelope = Te(tx=tx, signatures=None, network_id="TESTNET")

    envelope.sign(receiving_account)

    xdr_envelope = envelope.xdr()
    response = horizon.submit(xdr_envelope)
    print(response)
    if 'result_xdr' in response:
        print('Successful')
    else:
        print('Things go Fishy')


if __name__ == '__main__':
    at=Asset(code='ICO', issuer='GBWCKLXG6WE4VRC2WBUV3CNLUZBKFR6NZRSXXO4DRCFAIBF3OJJVB2VU')
    opr_change_trust(at,
            "GBK6PXRTUQ3GJTQHS5EIMF5NLCTGABBOGD33UR5TCAJ3B5WAK4R3SH2P",
            "SA7XSKQTSOHOXGCFYPFVYXTG55ZHKFL4WUFC5QEESZTIBDW5NKFUEM52"
    )
