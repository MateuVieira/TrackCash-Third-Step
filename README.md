# TrackCash-Third-Step

<h1 align="center">
  <img alt="TackCash" title="TackCash" src="https://scontent-gru2-2.cdninstagram.com/v/t51.2885-19/s320x320/75487952_484171055518655_7311530687218057216_n.jpg?_nc_ht=scontent-gru2-2.cdninstagram.com&_nc_ohc=099peI-odLgAX_zbfBM&oh=29e463dac08cd8f05f4b2511dbc85bbf&oe=5FB200AE" width="300px" />
</h1>

### Tech

Este projeto foi feito utilizando as seguintes tecnologias:

* Python - version 3.8.5
* Pandas - version 1.1.3

### Inicializar

Dentro do diretório raiz deste repositorio, rodar o comando para executar o script

```sh
$ python3 thirdStep.py
```
### Descrição

Este projeto foi proposto como um teste para a avaliação das habilidades com o uso da linguagem de programação Python e da biblioteca Pandas, para a leitura e processamento de um arquivo. O arquivo está dentro do diretório Data na raiz deste repositório.

Foi pedido que os dados fossem disposto para o usuário segundo a tabela abaixo:

| Data da transação | ID do pedido Seller| Método de pagamento |Comissão ML por parcela|Valor bruto da parcela|% Comissão|Conciliação|
|:-------------:|:-------------:|:-----:|:-----:|:-----:|:-----:|:-----:|

A coluna Conciliação desta tabela é gerada com base em três regras, definidas pelo método de pagamento utilizado:
* Cartão de crédito e boleto = Conciliação receberá o resultado do teste lógico (Valor bruto da parcela * % Comissão) corresponde ao valor de Comissão ML por parcela, se positivo imprime “conciliado” do contrário não conciliado
* Estorno = Conciliação receberá o resultado do teste lógico (Valor bruto do pedido* % Comissão) corresponde ao valor de Valor líquido da parcela, se positivo imprime “conciliado” do contrário não conciliado
* Transferência = Comissão ML por parcela recebe Valor da antecipação e Valor bruto da parcela recebe Valor líquido da parcela, Conciliação recebe “Retirada” quando Valor da antecipação for maior que 0 e “Movimentação” do contrário.  

O último ponto abordado neste projeto foi realizar uma pequena extração dos dados para mostrar para o usuário o número total de linhas processadas, as informações da coluna de Conciliação e as informações da coluna de métodos de pagamento, mostrando os números totais de cada campo, como também é informada a porcentagem dos tipos de itens que constituem a informação da coluna.
