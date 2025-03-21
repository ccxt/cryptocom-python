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

### Sync

```Python
from crypto_com_sdk import CryptocomSync

def main():
    instance = CryptocomSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)
```

### Async

```Python
import asyncio
from crypto_com_sdk import CryptocomAsync

async def main():
    instance = CryptocomAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

asyncio.run(main())
```

### Websockets

```Python
from crypto_com_sdk import CryptocomWs

async def main():
    instance = CryptocomWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")
```

