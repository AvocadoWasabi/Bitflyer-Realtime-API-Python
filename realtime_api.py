import json
import websocket
from time import sleep
from logging import getLogger,INFO,StreamHandler
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)

"""
This program calls Bitflyer real time API JSON-RPC2.0 over Websocket
"""
class RealtimeAPI(object):

    def __init__(self, url, channel):
        self.url = url
        self.channel = channel

        #Define Websocket
        self.ws = websocket.WebSocketApp(self.url,header=None,on_open=self.on_open, on_message=self.on_message, on_error=self.on_error, on_close=self.on_close)
        websocket.enableTrace(True)
        self.ws.keep_running = True

    def run(self):
        #ws has loop. To break this, set keep_running=False from outside
        self.ws.run_forever()   
        logger.info('Web Socket process ended.')

    def stop(self):
        self.ws.keep_running = False
        logger.info('Stop Web Socket Connection')

    """
    Below are callback functions of websocket.
    """
    # when we get message
    def on_message(self, ws, message):
        output = json.loads(message)['params']
        logger.info(output)

    # when error occurs
    def on_error(self, ws, error):
        logger.error(error)

    # when websocket closed.
    def on_close(self, ws):
        logger.info('disconnected streaming server')

    # when websocket opened.
    def on_open(self, ws):
        logger.info('connected streaming server')
        output_json = json.dumps(
            {'method' : 'subscribe',
            'params' : {'channel' : self.channel}
            }
        )
        ws.send(output_json)

if __name__ == '__main__':
    #API endpoint
    url = 'wss://ws.lightstream.bitflyer.com/json-rpc'
    """
    Bitflyer board channel
    list :
    lightning_board_snapshot_<productCode>
    lightning_board_<productCode>
    lightning_ticker_<productCode>
    lightning_executions_<product_code>
    for detail see
    https://lightning.bitflyer.jp/docs?lang=en
    https://lightning.bitflyer.jp/docs?lang=ja

    product code of spot_trading is "BTC_JPY"
    """
    channel = 'lightning_board_snapshot_BTC_JPY'
    json_rpc = RealtimeAPI(url=url, channel=channel)
    json_rpc.run()

    while True:
        try:
            sleep(0.1)
        except KeyboardInterrupt:
            json_rpc.stop()
            exit()
            