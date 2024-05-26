import time
import os
import csv

import shioaji as sj
from shioaji import TickFOPv1, BidAskFOPv1, Exchange
import pandas as pd
import configparser

class Quant:
    def __init__(self):

        self.API_Key=0
        self.SecreatKey=0
        self.API=sj.Shioaji()
        self.account=0
        self.time=0
        self.configread("API_Key.ini", chkFileExist=True)


    def configread(self, configfile, chkFileExist):
        if chkFileExist and not os.path.isfile(configfile):
            raise FileExistsError("File %s not exist!" % configfile)
        
        config = configparser.ConfigParser()
        config.read(configfile)
        self.API_Key=config['API_Key']['Key']
        self.SecreatKey=config['API_Key']['SecreatKEY']

        print('Your API Key is', self.API_Key)
        print('Your Secreat Key is', self.SecreatKey)

    def logIn(self):
        self.account =  self.API.login(self.API_Key, self.SecreatKey)

    def logOut(self):
        Ack = self.API.logout()
        print(Ack)
    
    def structTime(self, Time):
        struct_time = time.strptime(Time, "%Y-%m-%d %H:%M:%S") # 轉成時間元組
        print(struct_time)
        return struct_time
    
    def formatTime(self, Time):
        struct_time = self.structTime(Time)
        # fill up time structure
        dateFillup = f"{struct_time.tm_year}-{str(struct_time.tm_mon).zfill(2)}-{str(struct_time.tm_mday).zfill(2)}"
        TimeFillup = f"{str(struct_time.tm_hour).zfill(2)}:{str(struct_time.tm_min).zfill(2)}:{str(struct_time.tm_sec).zfill(2)}"

        return (dateFillup, TimeFillup)
    
    def getStockHistroy(self, stockCode, startTime, endTime):
        pd.set_option('display.max_columns', None)
        ticks=None
        
        struct_date_Start, struct_time_Start = Q.formatTime(time_Start)
        struct_date_End, struct_time_End = Q.formatTime(time_End)

        match stockCode:
            case '2330':   # TSMC
                TSE2330 = self.API.Contracts.Stocks.TSE.TSE2330
                ticks = self.API.ticks(
                    contract=TSE2330,
                    date=struct_date_Start,
                    query_type=sj.constant.TicksQueryType.RangeTime,
                    time_start=struct_time_Start,
                    time_end=struct_time_End)
            case 'TXFR1': 
                ticks = self.API.ticks(
                    contract=self.API.Contracts.Futures.TXF.TXFR1,
                    date=struct_date_Start,
                    query_type=sj.constant.TicksQueryType.RangeTime,
                    time_start=struct_time_Start,
                    time_end=struct_time_End)
            case 'TXFR2': 
                ticks = self.API.ticks(
                    contract=self.API.Contracts.Futures.TXF.TXFR2,
                    date=struct_date_Start,
                    query_type=sj.constant.TicksQueryType.RangeTime,
                    time_start=struct_time_Start,
                    time_end=struct_time_End)
        
        df = pd.DataFrame({**ticks})
        df.ts = pd.to_datetime(df.ts)
        print(df.tail(10))

    # @api.on_tick_fop_v1()
    def quote_callback(exchange: Exchange, tick: TickFOPv1):
        print(f"Exchange: {exchange}, Tick: {tick}")


    # @api.on_bidask_fop_v1()
    def quote_callback(exchange: Exchange, bidask: BidAskFOPv1):
        print(f"Exchange: {exchange}, BidAsk: {bidask}")


    # @api.quote.on_event
    def event_callback(resp_code: int, event_code: int, info: str, event: str):
        print(f'Response code: {resp_code} | Event code: {event_code} | Event: {event}')


# api = sj.Shioaji()

# accounts =  api.login("9wA3Wos5ZAeSgqZjqwp81whvhGMnXLQMun9ixH5Qdzoi", "5i1jXikWsFCxbLUtMjrL53Fi28wpFrT9F8kBzE8BC5K6")

# TSE2330 = api.Contracts.Stocks.TSE.TSE2330
# ticks = api.ticks(
#     contract=TSE2330,
#     date="2021-10-13",
#     query_type=sj.constant.TicksQueryType.RangeTime,
#     time_start="13:24:00",
#     time_end="13:24:30"
# )

# pd.set_option('display.max_columns', None)

# df = pd.DataFrame({**ticks})
# df.ts = pd.to_datetime(df.ts)

# print(df.tail(10))


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

# print("台指期近月: {}".format(api.Contracts.Futures.TXF.TXFR1))
# print("台指期次月: {}".format(api.Contracts.Futures.TXF.TXFR2))

# api.activate_ca(
#     ca_path="C:\\ekey\\551\\N125020171\\S",
#     ca_passwd="Pds992dc",
#     person_id="N125020171",
# )

if __name__ == '__main__':
    # api = sj.Shioaji()
    # accounts =  api.login("9wA3Wos5ZAeSgqZjqwp81whvhGMnXLQMun9ixH5Qdzoi", "5i1jXikWsFCxbLUtMjrL53Fi28wpFrT9F8kBzE8BC5K6")

    # TSE2330 = api.Contracts.Stocks.TSE.TSE2330
    # ticks = api.ticks(
    #     contract=TSE2330,
    #     date="2021-10-13",
    #     query_type=sj.constant.TicksQueryType.RangeTime,
    #     time_start="13:24:00",
    #     time_end="13:24:30"
    # )

    # pd.set_option('display.max_columns', None)

    # df = pd.DataFrame({**ticks})
    # df.ts = pd.to_datetime(df.ts)

    # print(df.tail(10))
    # api.logout()
    
    
    Q = Quant()
    Q.logOut()
    Q.logIn()

    time_Start = "2024-05-24 13:00:00" # 時間格式為字串
    time_End= "2024-05-24 13:00:30" # 時間格式為字串
    
    Q.getStockHistroy('2330', time_Start, time_End)

    print('End of script')


    # msg = T4.init_t4(UserInfo['UserId'], UserInfo['Password'], '')
    # print(msg)