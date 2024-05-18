var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end("Welcome to Kubernetes~! by AWS Cloud School 4th." + "\n");
}).listen(8080);
