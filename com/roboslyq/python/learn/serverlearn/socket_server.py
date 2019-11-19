import socketserver


# 创建socketserver.BaseRequestHandler子类
class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024)
                print("{} send:".format(self.client_address), self.data)
                if not self.data:
                    print("connection lost")
                    break
                self.request.sendall(self.data.upper())
        except Exception as e:
            print(self.client_address, "连接断开")
        finally:
            self.request.close()

    def setup(self):
        print("before handle,连接建立：", self.client_address)

    def finish(self):
        print("finish run  after handle")


if __name__ == "__main__":
    # 多个变量一同时定义
    HOST, PORT = "localhost", 9999
    # 创建Socket服务，传入回调类：TCPHandler
    server = socketserver.TCPServer((HOST, PORT), TCPHandler)

    server.serve_forever()
