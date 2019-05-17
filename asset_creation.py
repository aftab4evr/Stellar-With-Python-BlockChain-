from stellar_base.asset import Asset
def create_asset(code, issuer_address):
    asset = Asset(code, issuer_address)
    return asset
if __name__ == '__main__':
    ISSUER_ADDRESS = 'GDMW2O6J4CLMKV7BIM2ZIOFY4UAGQ7NAH3SR4Q23YDZUXY5WSXWWALKN'
    ISSUER_SEED = 'SBT6AJR62ILZWVJSPKZLLS37RC6P3Z5OTHVPPKA3NCTYGO6LBLWNQGVO'
    ASSET_CODE = 'MOB'
    new_asset = create_asset(ASSET_CODE,ISSUER_ADDRESS)
    print(new_asset.__dict__)