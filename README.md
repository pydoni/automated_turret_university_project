<h1>projeto_completamente_etico</h1>

<hr>
<h3 align="center">Integrantes:</h3>

<h4 align="center">19.00102-9 Vinicius Abe de Godoy </h4>
<h4 align="center">19.00499-0 Fernando Padilha Farah </h4>
<h4 align="center">19.02482-7 Pedro Henrique Ferreira Dominichelli Fabris</h4>
<h4 align="center">17.02005-0 Pedro Henrique Soares Pinheiro</h4>

<hr>

Projeto para a matéria de Microcontroladores e dispositivos embarcados.

O projeto é uma turreta automatica que mira autoamticamente no alvo desejado.

<hr><br>
<p align="center"><img src="https://media0.giphy.com/media/2EsTvCgsu7f8elN6Vw/giphy.gif?cid=790b761184322891491c7c6e40043d4a1727378b0ed920b8&rid=giphy.gif&ct=g" align="center"></p>
<p align="center">Prototipo v1</p>

A sua primeira versão foi criado para os testes de movimentação em dois eixos com o uso de servos e estudo da estrutura mecânica.
O movimento era realizado de forma manual, com o auxilio de dois potênciometros.



<hr><br>
<p align="center"><img width = 300 src="https://i.imgur.com/nA68DKk.jpg" align="center"></p>
<p align="center">Prototipo v2</p>

A segunda versão teve a sua estrutura revisada e realiza a mira automática através de um camera que envia fotos do local para 
um computador que realiza a inferência de detecção do tipo de alvo desejado, enviando via comunicação serial uma chamada de função
no pico pi com os angulos de cada servo, para a realização da mira.

A inferência de detecção de objeto é realizada através de uma versão modificada do framework YoloV5, com as classes utilizadas como
alvo sendo treinadas no COCO dataset.
<br>
<a href="https://youtu.be/z4mhUnOfTGA"> <b>Link do video de funcionamento</b></a>
<hr>
<p align="center"> Diagrama elétrico em blocos</p>
<p align="center"><img src="https://i.imgur.com/ngjK5ji.jpg" align="center"></p>
<br>
<hr>
<p align="center"> Fluxograma do processo de mira</p>
<p align="center"><img src="https://i.imgur.com/i3mpWe8.jpg" align="center"></p>
<br>

