# cryptocom-python
Python SDK (sync and async) for Cryptocom with Rest and WS capabilities.

You can check Cryptocom's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/cryptocom)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install crypto-com-sdk
```

## Usage

### Async

```Python
from crypto_com_sdk import CryptocomAsync

async def main():
    instance = CryptocomAsync({})
    order = await instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Sync

```Python
from crypto_com_sdk import CryptocomSync

def main():
    instance = CryptocomSync({})
    order =  instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Websockets

```Python
from crypto_com_sdk import CryptocomWs

async def main():
    instance = CryptocomWs({})
    while True:
        orders = await instance.watch_orders(__EXAMPLE_SYMBOL__)
```

