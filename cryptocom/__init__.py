import sys
import cryptocom.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from cryptocom.ccxt import cryptocom as CryptocomSync
from cryptocom.ccxt.async_support.cryptocom import cryptocom as CryptocomAsync
from cryptocom.ccxt.pro.cryptocom import cryptocom as CryptocomWs
