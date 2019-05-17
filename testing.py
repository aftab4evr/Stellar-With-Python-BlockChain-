import time

from stellar_base.keypair import Keypair
from stellar_base.builder import Builder

alice_seed = 'SBRGXEJOGS6CHY67TR5BZXDE23GWSXTLIGTSH4IEU4JSCCLUS6FPWXSC'  # GCDCDLVJNSLJWWHH2Q36IGBYZP6O6MFZOMXSW2DNBUCWKZDCRTIT73DP
bob_seed = 'SC34JMOSP24N3ELLEVNJD662TII7YVFG7CJI57GBE3BS2WG2IHTIQDFT'  # GCNT7JJDVQ5ZAZ4OLHXUJPONYATFE5YOTRTKMPI2EQCGU2SK4QGCETJ5
dav_seed = 'SA5HW5RYBG34FUIGHPE7RHIZKY5FMVGE7CKZZHOIMEOKAHWU6M7CZAMZ'  # GCPITREYLKN3WHVPYBM7SNW2V7ZPYYPZHARPBWEC3XTZASUI3MGFYLWF
eve_address = 'GALT7IJPOR37NJFXFBD4ZYME5C23KXTVQTB4XHY3CQ2LPJJRP3VXR4AS'

alice_kp = Keypair.from_seed(alice_seed)
bob_kp = Keypair.from_seed(bob_seed)
dav_kp = Keypair.from_seed(dav_seed)


def setup_threshold():
    builder = Builder(dav_seed).append_set_options_op(
        source=dav_kp.address().decode(),
        high_threshold=3,
        med_threshold=3,
        low_threshold=3,
        master_weight=1,
        signer_type='ed25519PublicKey',
        signer_weight=1,
        signer_address=alice_kp.address().decode()
    ).append_set_options_op(
        source=dav_kp.address().decode(),
        signer_type='ed25519PublicKey',
        signer_weight=1,
        signer_address=bob_kp.address().decode()
    )  # append more signers here
    builder.sign()
    resp = builder.submit()
    return resp


def payment():
    min_time = int(time.time()) - 10
    max_time = min_time + 100
    time_bounds = {'minTime': min_time, 'maxTime': max_time}
    builder = Builder(dav_seed).add_time_bounds(time_bounds=time_bounds) \
        .append_payment_op(destination=eve_address, amount='100', asset_code='XLM', asset_issuer=None)
    builder.sign()  # signed by dav with default seed
    builder.sign(alice_seed)  # signed by alice
    builder.sign(bob_seed)  # signed by bob
    resp = builder.submit()
    return resp


if __name__ == '__main__':
    print(setup_threshold())
    print(payment())