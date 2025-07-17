# cryptocom-python
Python SDK (sync and async) for Cryptocom cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/cryptocom)
- You can check Cryptocom's docs here: [Docs](https://www.google.com/search?q=google+cryptocom+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/cryptocom-python
- Pypi package: https://pypi.org/project/crypto-com-sdk


## Installation

```
pip install crypto-com-sdk
```

## Usage

### Sync

```Python
from cryptocom import CryptocomSync

def main():
    instance = CryptocomSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

main()
```

### Async

```Python
import sys
import asyncio
from cryptocom import CryptocomAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = CryptocomAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from cryptocom import CryptocomWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = CryptocomWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_advanced_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `fetch_accounts(self, params={})`
- `fetch_balance(self, params={})`
- `fetch_currencies(self, params={})`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposit_addresses_by_network(self, code: str, params={})`
- `fetch_deposit_withdraw_fees(self, codes: Strings = None, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ledger(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_position(self, symbol: str, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_settlement_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_trading_fee(self, symbol: str, params={})`
- `fetch_trading_fees(self, params={})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders_for_symbols(self, orders: List[CancellationRequest], params={})`
- `cancel_orders(self, ids, symbol: Str = None, params={})`
- `close_position(self, symbol: str, side: OrderSide = None, params={})`
- `custom_handle_margin_mode_and_params(self, methodName, params={})`
- `describe(self)`
- `edit_order_request(self, id: str, symbol: str, amount: float, price: Num = None, params={})`
- `edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `nonce(self)`
- `params_to_string(self, object, level)`
- `withdraw(self, code: str, amount: float, address: str, tag=None, params={})`

### REST Raw

- `base_public_get_v1_public_get_announcements(request)`
- `v1_public_get_public_auth(request)`
- `v1_public_get_public_get_instruments(request)`
- `v1_public_get_public_get_book(request)`
- `v1_public_get_public_get_candlestick(request)`
- `v1_public_get_public_get_trades(request)`
- `v1_public_get_public_get_tickers(request)`
- `v1_public_get_public_get_valuations(request)`
- `v1_public_get_public_get_expired_settlement_price(request)`
- `v1_public_get_public_get_insurance(request)`
- `v1_public_get_public_get_risk_parameters(request)`
- `v1_public_post_public_staking_get_conversion_rate(request)`
- `v1_private_post_private_set_cancel_on_disconnect(request)`
- `v1_private_post_private_get_cancel_on_disconnect(request)`
- `v1_private_post_private_user_balance(request)`
- `v1_private_post_private_user_balance_history(request)`
- `v1_private_post_private_get_positions(request)`
- `v1_private_post_private_create_order(request)`
- `v1_private_post_private_amend_order(request)`
- `v1_private_post_private_create_order_list(request)`
- `v1_private_post_private_cancel_order(request)`
- `v1_private_post_private_cancel_order_list(request)`
- `v1_private_post_private_cancel_all_orders(request)`
- `v1_private_post_private_close_position(request)`
- `v1_private_post_private_get_order_history(request)`
- `v1_private_post_private_get_open_orders(request)`
- `v1_private_post_private_get_order_detail(request)`
- `v1_private_post_private_get_trades(request)`
- `v1_private_post_private_change_account_leverage(request)`
- `v1_private_post_private_get_transactions(request)`
- `v1_private_post_private_create_subaccount_transfer(request)`
- `v1_private_post_private_get_subaccount_balances(request)`
- `v1_private_post_private_get_order_list(request)`
- `v1_private_post_private_create_withdrawal(request)`
- `v1_private_post_private_get_currency_networks(request)`
- `v1_private_post_private_get_deposit_address(request)`
- `v1_private_post_private_get_accounts(request)`
- `v1_private_post_private_get_withdrawal_history(request)`
- `v1_private_post_private_get_deposit_history(request)`
- `v1_private_post_private_get_fee_rate(request)`
- `v1_private_post_private_get_instrument_fee_rate(request)`
- `v1_private_post_private_staking_stake(request)`
- `v1_private_post_private_staking_unstake(request)`
- `v1_private_post_private_staking_get_staking_position(request)`
- `v1_private_post_private_staking_get_staking_instruments(request)`
- `v1_private_post_private_staking_get_open_stake(request)`
- `v1_private_post_private_staking_get_stake_history(request)`
- `v1_private_post_private_staking_get_reward_history(request)`
- `v1_private_post_private_staking_convert(request)`
- `v1_private_post_private_staking_get_open_convert(request)`
- `v1_private_post_private_staking_get_convert_history(request)`
- `v2_public_get_public_auth(request)`
- `v2_public_get_public_get_instruments(request)`
- `v2_public_get_public_get_book(request)`
- `v2_public_get_public_get_candlestick(request)`
- `v2_public_get_public_get_ticker(request)`
- `v2_public_get_public_get_trades(request)`
- `v2_public_get_public_margin_get_transfer_currencies(request)`
- `v2_public_get_public_margin_get_load_currenices(request)`
- `v2_public_get_public_respond_heartbeat(request)`
- `v2_private_post_private_set_cancel_on_disconnect(request)`
- `v2_private_post_private_get_cancel_on_disconnect(request)`
- `v2_private_post_private_create_withdrawal(request)`
- `v2_private_post_private_get_withdrawal_history(request)`
- `v2_private_post_private_get_currency_networks(request)`
- `v2_private_post_private_get_deposit_history(request)`
- `v2_private_post_private_get_deposit_address(request)`
- `v2_private_post_private_export_create_export_request(request)`
- `v2_private_post_private_export_get_export_requests(request)`
- `v2_private_post_private_export_download_export_output(request)`
- `v2_private_post_private_get_account_summary(request)`
- `v2_private_post_private_create_order(request)`
- `v2_private_post_private_cancel_order(request)`
- `v2_private_post_private_cancel_all_orders(request)`
- `v2_private_post_private_create_order_list(request)`
- `v2_private_post_private_get_order_history(request)`
- `v2_private_post_private_get_open_orders(request)`
- `v2_private_post_private_get_order_detail(request)`
- `v2_private_post_private_get_trades(request)`
- `v2_private_post_private_get_accounts(request)`
- `v2_private_post_private_get_subaccount_balances(request)`
- `v2_private_post_private_create_subaccount_transfer(request)`
- `v2_private_post_private_otc_get_otc_user(request)`
- `v2_private_post_private_otc_get_instruments(request)`
- `v2_private_post_private_otc_request_quote(request)`
- `v2_private_post_private_otc_accept_quote(request)`
- `v2_private_post_private_otc_get_quote_history(request)`
- `v2_private_post_private_otc_get_trade_history(request)`
- `v2_private_post_private_otc_create_order(request)`
- `derivatives_public_get_public_auth(request)`
- `derivatives_public_get_public_get_instruments(request)`
- `derivatives_public_get_public_get_book(request)`
- `derivatives_public_get_public_get_candlestick(request)`
- `derivatives_public_get_public_get_trades(request)`
- `derivatives_public_get_public_get_tickers(request)`
- `derivatives_public_get_public_get_valuations(request)`
- `derivatives_public_get_public_get_expired_settlement_price(request)`
- `derivatives_public_get_public_get_insurance(request)`
- `derivatives_private_post_private_set_cancel_on_disconnect(request)`
- `derivatives_private_post_private_get_cancel_on_disconnect(request)`
- `derivatives_private_post_private_user_balance(request)`
- `derivatives_private_post_private_user_balance_history(request)`
- `derivatives_private_post_private_get_positions(request)`
- `derivatives_private_post_private_create_order(request)`
- `derivatives_private_post_private_create_order_list(request)`
- `derivatives_private_post_private_cancel_order(request)`
- `derivatives_private_post_private_cancel_order_list(request)`
- `derivatives_private_post_private_cancel_all_orders(request)`
- `derivatives_private_post_private_close_position(request)`
- `derivatives_private_post_private_convert_collateral(request)`
- `derivatives_private_post_private_get_order_history(request)`
- `derivatives_private_post_private_get_open_orders(request)`
- `derivatives_private_post_private_get_order_detail(request)`
- `derivatives_private_post_private_get_trades(request)`
- `derivatives_private_post_private_change_account_leverage(request)`
- `derivatives_private_post_private_get_transactions(request)`
- `derivatives_private_post_private_create_subaccount_transfer(request)`
- `derivatives_private_post_private_get_subaccount_balances(request)`
- `derivatives_private_post_private_get_order_list(request)`

### WS Unified

- `describe(self)`
- `pong(self, client, message)`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `un_watch_order_book(self, symbol: str, params={})`
- `watch_order_book_for_symbols(self, symbols: List[str], limit: Int = None, params={})`
- `un_watch_order_book_for_symbols(self, symbols: List[str], params={})`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `un_watch_trades(self, symbol: str, params={})`
- `watch_trades_for_symbols(self, symbols: List[str], since: Int = None, limit: Int = None, params={})`
- `un_watch_trades_for_symbols(self, symbols: List[str], params={})`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_ticker(self, symbol: str, params={})`
- `un_watch_ticker(self, symbol: str, params={})`
- `watch_tickers(self, symbols: Strings = None, params={})`
- `un_watch_tickers(self, symbols: Strings = None, params={})`
- `watch_bids_asks(self, symbols: Strings = None, params={})`
- `watch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `un_watch_ohlcv(self, symbol: str, timeframe='1m', params={})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_positions(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `set_positions_cache(self, client: Client, type, symbols: Strings = None)`
- `load_positions_snapshot(self, client, messageHash)`
- `watch_balance(self, params={})`
- `create_order_ws(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `edit_order_ws(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `cancel_order_ws(self, id: str, symbol: Str = None, params={})`
- `cancel_all_orders_ws(self, symbol: Str = None, params={})`
- `watch_public(self, messageHash, params={})`
- `watch_public_multiple(self, messageHashes, topics, params={})`
- `un_watch_public_multiple(self, topic: str, symbols: List[str], messageHashes: List[str], subMessageHashes: List[str], topics: List[str], params={}, subExtend={})`
- `watch_private_request(self, nonce, params={})`
- `watch_private_subscribe(self, messageHash, params={})`
- `authenticate(self, params={})`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.