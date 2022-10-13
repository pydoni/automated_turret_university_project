import serial # importação da biblioteca PySerial utilizada para comunicação serial


class Talker:

    def __init__(self):
        # Abertura da comunicação serial via usb, na frequência 9600
        self.serial = serial.Serial('/dev/ttyACM0', 9600, timeout=1, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

    def send(self, text: str):
        line = '%s\r\f' % text # formatação da conteudo a ser enviado
        self.serial.write(line.encode('utf-8')) #Envio de comando via serial convertido para bits em utf-8
        
        #teste para verificação se o pacote enviado chegou corretamente
        reply = self.receive()
        reply = reply.replace('>>> ','')
        if reply != text:
            raise ValueError('expected %s got %s' % (text, reply))

    def receive(self) -> str:
        #função para receber retorno do terminal repl da Micro PI codificando a chamado em bits separando por linha e decodificando a resposta no format utf-8
        line = self.serial.read_until('\r'.encode('UTF8')
        return line.decode('UTF8').strip()

    def close(self):
        self.serial.close() # encerramento de comunicação serial
