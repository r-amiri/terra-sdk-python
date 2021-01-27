from terra_sdk.key.mnemonic import MnemonicKey

from .lcd import LCDClient, Wallet

__all__ = ["LOCALTERRA_MNEMONICS", "LocalTerra"]

LOCALTERRA_MNEMONICS = {
    "validator": "satisfy adjust timber high purchase tuition stool faith fine install that you unaware feed domain license impose boss human eager hat rent enjoy dawn",
    "test1": "notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius",
    "test2": "quality vacuum heart guard buzz spike sight swarm shove special gym robust assume sudden deposit grid alcohol choice devote leader tilt noodle tide penalty",
    "test3": "symbol force gallery make bulk round subway violin worry mixture penalty kingdom boring survey tool fringe patrol sausage hard admit remember broken alien absorb",
    "test4": "bounce success option birth apple portion aunt rural episode solution hockey pencil lend session cause hedgehog slender journey system canvas decorate razor catch empty",
    "test5": "second render cat sing soup reward cluster island bench diet lumber grocery repeat balcony perfect diesel stumble piano distance caught occur example ozone loyal",
    "test6": "spatial forest elevator battle also spoon fun skirt flight initial nasty transfer glory palm drama gossip remove fan joke shove label dune debate quick",
    "test7": "noble width taxi input there patrol clown public spell aunt wish punch moment will misery eight excess arena pen turtle minimum grain vague inmate",
    "test8": "cream sport mango believe inhale text fish rely elegant below earth april wall rug ritual blossom cherry detail length blind digital proof identify ride",
    "test9": "index light average senior silent limit usual local involve delay update rack cause inmate wall render magnet common feature laundry exact casual resource hundred",
    "test10": "prefer forget visit mistake mixture feel eyebrow autumn shop pair address airport diesel street pass vague innocent poem method awful require hurry unhappy shoulder",
}

# TODO: add gas estimation
LOCALTERRA_DEFAULTS = {"url": "http://localterra:1317", "chain_id": "localterra"}


class LocalTerra(LCDClient):

    wallets: Dict[str, Wallet]

    def __init__(self, *args, **kwargs):
        options = {**LOCALTERRA_DEFAULTS, **kwargs}
        super().__init__(*args, **options)
        self.wallets = {
            wallet_name: self.wallet(
                MnemonicKey(mnemonic=LOCALTERRA_MNEMONICS[wallet_name])
            )
            for wallet_name in LOCALTERRA_MNEMONICS
        }