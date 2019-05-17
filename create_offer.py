from stellar_base.builder import Builder

bob_address = 'GBVS3DRQRIMCZW5AGYPJOHFMHIQADTEIJICRZ475OWG25FPLPGHW77IC'
alice_seed = 'SAPGVLD52VW6LMFNAI2YJJZRPWNBQRLKTLKAEFDFHOTP36Y45IVJ2GSB'

selling_code = 'XLM'
selling_issuer = None

buying_code = "YourAssetCode",  #asset_code="ICO"
buying_issuer = 'Put-Your-Reciver-Public-Key-Here'

price = '5.5'
amount = '12.5'

builder = Builder(secret=alice_seed, horizon_uri='https://horizon-testnet.stellar.org') \
             .append_manage_offer_op(selling_code, selling_issuer, buying_code, \
              buying_issuer, amount, price)
print(builder)
builder.sign()
builder.submit()