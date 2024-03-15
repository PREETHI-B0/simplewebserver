from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<h2>Top Five Software Companies with  Revenue</h2>
<head>
<body>
<table border="1">
  <tr>
    <th>Rank</th>
    <th>Company</th>
    <th>Revenue (in billions USD)</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Microsoft</td>
    <td>143.0</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Apple</td>
    <td>274.5</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Amazon</td>
    <td>386.1</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Google</td>
    <td>182.4</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Facebook</td>
    <td>85.9</td>
  </tr>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()