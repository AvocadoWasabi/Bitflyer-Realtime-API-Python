日本語版はREADME.mdを参照してください。

# Bitflyer-Realtime-API-Python
This is a sample program which call s BitFlyer Realtime API by Python.
(Bitflyer is a one of Bit-coin exchange point.)

There is 3 way to call realtime API,ands this program uses one of them,
JSON-RPC2.0 over Websocket.

## Basic Behavior
This program uses websocket library for connection.
On connection, the callback function "on_open" is called.
It sends subscription channel as JSON.
Then broadcasting starts.

The contents can be got with call back function "on_message" as JSON.

## Subscription channel
This is determined by what kind of information you want and what kind of board(spot trading, FX, futures) you select.
Ex. Spot trading and snap shot of board infomation,
lightning_board_snapshot_BTC_JPY

For detail, see Bitflyer official page
https://lightning.bitflyer.jp/docs?lang=en

## Lisence
Public Domain.
You can change, destribute and use commercial freely, at your own risk.
