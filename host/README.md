<h1>Funcionamento do Host</h1>

O Host é responsável pela realização da inferência dos alvos e comandar uma pico Pi que é responsável pelo controle lógico dos servos.

A inferência é realizada através do framework YoloV5, um framework popular python escrito em pytorch para a classificação de objetos,
via redes neurais convulacionais que seguem a arquitetura YOLO. Em nosso projeto fizemos uso de uma versão modificado por nós do script,
detect.py que é utilizado pra realizar inferência no framework, as modificações realizadas tem o intuito de fazer com que esse script seja,
responsável pela comunicação com a Pico Pi em tempo real, já que ele roda em videoStream fazendo a inferência a todo momento, dessa forma
a cada vez que um objeto de interesse é detectado, o script realiza a conexão com a Pico Pi através da criação de um objeto Talker, 
realiza as obtenções e cálculos necessários para a obtenção do angulo de cada servo e então via comunicação serial envia o comando para
realizar a movimentação dos servos, mirando no centro do alvo.

O alvo que foi utilizado para testes é a classe de celular, com os pesos obtidos pelo dataset público COCO.

O objeto Talker é descrito no script talker.py e é um objeto que utiliza da biblioteca PySerial para a realização de conexão serial,
envio de comandos com conversão em bits,obtenção de resposta do repl da Pico Pi e encerramento da conexão serial.

Para a realização de testes deve ser utilizado uma maquina linux, realizando um git clone do reposítorio da yolov5, substituindo o detect
dele pelo contido nesse diretório e colocando o talker.py dentro da mesma pasta. Rodando em sudo para evitar erros de permissão ao acesso serial.

Exemplo de comando:

python3 detect.py --source 0 --move-servo --max-det 1 --classes 77

<h2>Referências</h2>

github yolov5: https://github.com/ultralytics/yolov5

Comunicação serial usb em python : https://blog.rareschool.com/2021/01/controlling-raspberry-pi-pico-using.html
