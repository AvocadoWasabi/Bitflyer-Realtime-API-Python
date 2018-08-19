See README-en.md for English description.

Bitflyer-Realtime-API-Python
これは仮想通貨取引所であるBitflyerのRealtime APIをPythonで呼び出すサンプルプログラムです。

Realtime APIを呼び出す方法はいくつかの種類がありますが、 その中のJSON-RPC2.0 over WebSocketを利用しています。

基本動作
websocket-clientライブラリを用いて接続し、 接続時、on_openのコールバック関数が呼ばれた時点で、購読チャンネルをJSONで送信しています。 それによって、対応するチャンネルの情報(板情報など)が配信され、 配信されるたびにon_messageがよびだされ、そこで配信内容のJSONが受け渡しされます。

##購読チャンネル 取得したい情報と板(現物・FX・先物)によって規定されます。 例えば、現物の板情報のスナップだと、 lightning_board_snapshot_BTC_JPYとなります。 詳しくはBitflyer公式HPのAPIについてのページを参照してください。 https://lightning.bitflyer.jp/docs

ライセンス
このプログラムは著作権を一切放棄しています(Public Domain)。 改変・配布・商用利用は一切自由ですが、各自の責任においてご利用ください。
