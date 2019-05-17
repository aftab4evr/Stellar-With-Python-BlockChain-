from stellar_base.keypair import Keypair
from stellar_base.asset import Asset
from stellar_base.builder import Builder

issuing_secret = 'Put-Your-Secret-Key-Here'
issuing_public = Keypair.from_seed(issuing_secret).address().decode()

receiving_secret = 'Put-Your-Secret-Key-Here'
receiving_public = Keypair.from_seed(receiving_secret).address().decode()

my_asset = Asset('YourAssetCode', issuing_public)
builder = Builder(
    receiving_secret, network='TESTNET').append_trust_op(
        destination=my_asset.issuer,
        code=my_asset.code,
        limit="7000")
builder.sign()
resp = builder.submit()
print(resp)

#for trasfering the coin
builder = Builder(
    issuing_secret, network='TESTNET').append_payment_op(
        destination=receiving_public,
        amount='1000',
        asset_code="YourAssetCode",  #asset_code="ICO"
        asset_issuer=issuing_public)
builder.sign()
resp = builder.submit()
print(resp)