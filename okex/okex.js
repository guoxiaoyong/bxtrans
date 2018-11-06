const WebSocket = require('ws');

const URL = 'wss://real.okex.com:10440/websocket'
const ws = new WebSocket(URL);

ws.on('open', function open() {
  console.log('Connected!');
  params = {
    'event': 'addChannel',
    'channel': 'ok_sub_futureusd_btc_usd_depth_20',
  }
  ws.send(JSON.stringify(params))
});

ws.on('message', (msg) => {
   console.log(msg)
}
)
