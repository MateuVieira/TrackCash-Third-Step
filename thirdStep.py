import pandas as pd

def verifyConciliacao(data):
  paymentWay = data['Método de pagamento']

  if paymentWay == 'Boleto' or paymentWay == 'Cartão de Crédito':
    calcConciliacao = data['Valor bruto da parcela'] * data['% Comissão']
    return 'Conciliado' if calcConciliacao > 0 else 'Não Conciliado'

  if paymentWay == 'Estorno':
    return 'Conciliado' if data['Valor líquido da parcela'] > 0 else 'Não Conciliado'

  if paymentWay == 'Transferência':
    return 'Retirada' if data['Valor da antecipação'] > 0 else 'Movimentação'

def createColumnConciliacao(data):

  columnConciliacao = data.apply(verifyConciliacao, axis=1)

  return columnConciliacao

def verifyMl(data): 
  return data['Valor da antecipação'] if data['Método de pagamento'] == 'Transferência' else data['Comissão ML por parcela']

def verifyValorBruto(data): 
  return data['Valor líquido da parcela'] if data['Método de pagamento'] == 'Transferência' else data['Valor bruto da parcela']

def calcPorcentegeValue(value, total):
  return round((value/total) * 100, 2)

DATA_PATH = './Data/planilha_de_repasse.xlsx'
data = pd.read_excel(DATA_PATH)
dataSheets = pd.DataFrame(data)

dataSheets['Conciliação'] = createColumnConciliacao(dataSheets)

selectionTranferPayment = dataSheets['Método de pagamento'] == 'Transferência'

dataSheets['Comissão ML por parcela'] = dataSheets.apply(verifyMl, axis=1)
dataSheets['Valor bruto da parcela'] = dataSheets.apply(verifyValorBruto, axis=1)

print(dataSheets[[
  'Data da transação',
  'ID do pedido Seller',
  'Método de pagamento', 
  'Comissão ML por parcela',
  'Valor bruto da parcela',
  '% Comissão',
  'Conciliação',
  ]].head())

print('\n__Info__')

numberOfRows = len(dataSheets)
print(f'Número total de linhas: {numberOfRows}')

# Calculando o número de conciliação
infoConciliados = dataSheets['Conciliação'] == 'Conciliado'
infoNumeroConciliados = dataSheets[infoConciliados].shape[0]
infoPorcentageConciliados = calcPorcentegeValue(infoNumeroConciliados, numberOfRows)

# Calculando o número de não conciliação
infoNotConciliados = dataSheets['Conciliação'] == 'Não Conciliado'
infoNumeroNotConciliados = dataSheets[infoNotConciliados].shape[0]
infoPorcentageNotConciliados = calcPorcentegeValue(infoNumeroNotConciliados, numberOfRows)

# Calculando o número de Retiradas
infoRetirada = dataSheets['Conciliação'] == 'Retirada'
infoNumeroRetirada = dataSheets[infoRetirada].shape[0]
infoPorcentageRetirada = calcPorcentegeValue(infoNumeroRetirada, numberOfRows)

# Calculando o número de Movitações
infoMovimentacao = dataSheets['Conciliação'] == 'Movimentação'
infoNumeroMovimentacao = dataSheets[infoMovimentacao].shape[0]
infoPorcentageMovimentacao = calcPorcentegeValue(infoNumeroMovimentacao, numberOfRows)

print('\nNúmero de ocorrências coluna Conciliação:')
print(
f'Conciliados - {infoNumeroConciliados} - {infoPorcentageConciliados}% ' + 
f'| Não Conciliados - {infoNumeroNotConciliados} - {infoPorcentageNotConciliados}% ' + 
f'| Retiradas - {infoNumeroRetirada} -  {infoPorcentageRetirada}% ' + 
f'| Movimentações - {infoNumeroMovimentacao} - {infoPorcentageMovimentacao}% '
)

# Calculando o número de Boleto
infoPaymentWayBoleto = dataSheets['Método de pagamento'] == 'Boleto'
infoPaymentWayNumeroBoleto = dataSheets[infoPaymentWayBoleto].shape[0]
infoPaymentWayPorcentageBoleto = calcPorcentegeValue(infoPaymentWayNumeroBoleto, numberOfRows)

# Calculando o número de Cartão de Crédito
infoPaymentWayCard = dataSheets['Método de pagamento'] == 'Cartão de Crédito'
infoPaymentWayNumeroCard = dataSheets[infoPaymentWayCard].shape[0]
infoPaymentWayPorcentageCard = calcPorcentegeValue(infoPaymentWayNumeroCard, numberOfRows)

# Calculando o número de Estorno
infoPaymentWayEstorno = dataSheets['Método de pagamento'] == 'Estorno'
infoPaymentWayNumeroEstorno = dataSheets[infoPaymentWayEstorno].shape[0]
infoPaymentWayPorcentageEstorno = calcPorcentegeValue(infoPaymentWayNumeroEstorno, numberOfRows)

# Calculando o número de Transferência
infoPaymentWayTransferencia = dataSheets['Método de pagamento'] == 'Transferência'
infoPaymentWayNumeroTransferencia = dataSheets[infoPaymentWayTransferencia].shape[0]
infoPaymentWayPorcentageTransferencia = calcPorcentegeValue(infoPaymentWayNumeroTransferencia, numberOfRows)

print('\nNúmero de ocorrências coluna Método de pagamento:')
print(
f'Boleto - {infoPaymentWayNumeroBoleto} - {infoPaymentWayPorcentageBoleto}% ' + 
f'| Cartão de Crédito - {infoPaymentWayNumeroCard} - {infoPaymentWayPorcentageCard}% ' + 
f'| Estorno - {infoPaymentWayNumeroEstorno} - {infoPaymentWayPorcentageEstorno}% ' + 
f'| Transferência - {infoPaymentWayNumeroTransferencia} - {infoPaymentWayPorcentageTransferencia}% '
)