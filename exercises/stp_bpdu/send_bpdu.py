from socket import *
from struct import pack
class DummyBPDU():
    def __init__(self, *, dst_addr=b'\x01\x80\xC2\x00\x00\x00', src_addr=b'\x00'*6,  llc_header =b'\x42\x42\x03', payload = b'\x00\x00\x00\x80'):
        self.dst_addr = dst_addr
        self.src_addr = src_addr
        self.llc_header = llc_header
        self.payload = payload
        self.header = self.dst_addr + self.src_addr + pack('>H', len(self.llc_header) + len(self.payload)) + self.llc_header
        self.frame = self.header + self.payload

    def sendFrame(self,  interface):
        s = socket(AF_PACKET,  SOCK_RAW)
        s.bind((interface, 0))
        s.send(self.frame)

p = DummyBPDU()
p.sendFrame('eth0')