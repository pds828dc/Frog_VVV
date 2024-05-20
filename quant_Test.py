import time
import shioaji as sj
from shioaji import TickFOPv1, BidAskFOPv1, Exchange
import pandas as pd

# @api.on_tick_fop_v1()
def quote_callback(exchange: Exchange, tick: TickFOPv1):
    print(f"Exchange: {exchange}, Tick: {tick}")


# @api.on_bidask_fop_v1()
def quote_callback(exchange: Exchange, bidask: BidAskFOPv1):
    print(f"Exchange: {exchange}, BidAsk: {bidask}")


# @api.quote.on_event
def event_callback(resp_code: int, event_code: int, info: str, event: str):
    print(f'Response code: {resp_code} | Event code: {event_code} | Event: {event}')


api = sj.Shioaji()

accounts =  api.login("9wA3Wos5ZAeSgqZjqwp81whvhGMnXLQMun9ixH5Qdzoi", "5i1jXikWsFCxbLUtMjrL53Fi28wpFrT9F8kBzE8BC5K6")

TSE2330 = api.Contracts.Stocks.TSE.TSE2330
ticks = api.ticks(
    contract=TSE2330,
    date="2021-10-13",
    query_type=sj.constant.TicksQueryType.RangeTime,
    time_start="13:24:00",
    time_end="13:24:30"
)

pd.set_option('display.max_columns', None)

df = pd.DataFrame({**ticks})
df.ts = pd.to_datetime(df.ts)

print(df.tail(10))






# ftu_txfTXFR1 = api.Contracts.Futures.TXF.TXFR1

# api.quote.subscribe(
#     ftu_txfTXFR1,
#     quote_type=sj.constant.QuoteType.Tick,
#     version=sj.constant.QuoteVersion.v1
# )

# api.quote.subscribe(
#     ftu_txfTXFR1,
#     quote_type=sj.constant.QuoteType.BidAsk,
#     version=sj.constant.QuoteVersion.v1
# )

# i = 0
# while True:
#     while i < 10:
#         time.sleep(1)
#         i += 1
#     print("Sleep 10 second!")
#     i = 0
#     api.logout()





# print(accounts)

# stk_006204 = api.Contracts.Stocks.TSE.TSE006204
# print(stk_006204)

# print("台指期近一: {}".format(api.Contracts.Futures.TXF.TXFR1))
# print("台指期近二: {}".format(api.Contracts.Futures.TXF.TXFR2))

# api.activate_ca(
#     ca_path="C:\\ekey\\551\\N125020171\\S",
#     ca_passwd="Pds992dc",
#     person_id="N125020171",
# )

