from stellar_base.keypair import Keypair
from stellar_base.asset import Asset
from stellar_base.builder import Builder


issuing_secret = 'SBPUWEZLBUSD23S5UGUOMLDD5AKURT7DBYNVVTCBDEQ5UC65BBME6KUP'
issuing_public = Keypair.from_seed(issuing_secret).address().decode()

receiving_secret = 'SCUOYTGEYH2XBYBHIF2UBKV62J2BZ4Z6ES4BBCE4IFPMEBFHNQ7NVROS'
receiving_public = Keypair.from_seed(receiving_secret).address().decode()

my_asset = Asset('MOB', issuing_public)
builder = Builder(
    receiving_secret, network='TESTNET').append_trust_op(
        destination=my_asset.issuer,
        code=my_asset.code,
        limit="5000")
builder.sign()
resp = builder.submit()
print(resp)

builder = Builder(
    issuing_secret, network='TESTNET').append_payment_op(
        destination=receiving_public,
        amount='1000',
        asset_code="MOB",
        asset_issuer=issuing_public)
builder.sign()
resp = builder.submit()
print(resp)
