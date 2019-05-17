from stellar_base.asset import Asset
def create_asset(code, issuer_address):
    asset = Asset(code, issuer_address)
    return asset
if __name__ == '__main__':
    ISSUER_ADDRESS = ''
    ISSUER_SEED = '"Put-Your-Issuer-Secret-Key-Here'
    ASSET_CODE = 'YourAssetCode'
    new_asset = create_asset(ASSET_CODE,ISSUER_ADDRESS)
    print(new_asset.__dict__)