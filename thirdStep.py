import pandas as pd
import Constants


def verifyConciliacao(data):
  # Set payment way
  paymentWay = data[Constants.DATA_KEY_PAYMENT_WAY]

  # First check - payment method is "Cartão de Crédito" or "Boleto"
  if paymentWay == Constants.PAYMENT_WAY_BOLETO or paymentWay == Constants.PAYMENT_WAY_CARD:
    calcConciliacao = data[Constants.DATA_KEY_GROSS_AMOUNT] * data[Constants.DATA_KEY_COMMISSION]
    return Constants.CONCILIATION_OPTION_CONCILIATED if calcConciliacao > 0 else Constants.CONCILIATION_OPTION_NOT_CONCILIATED

  # Second check - payment method is "Estorno"
  if paymentWay == Constants.PAYMENT_WAY_ESTORNO:
    return Constants.CONCILIATION_OPTION_CONCILIATED if data[Constants.DATA_KEY_NET_VALUE] > 0 else Constants.CONCILIATION_OPTION_NOT_CONCILIATED

  # Third check - payment method is "Transferência"
  if paymentWay == Constants.PAYMENT_WAY_TRANSFERENCIA:
    return Constants.CONCILIATION_OPTION_WITHDRAWAL if data[Constants.DATA_KEY_ANTICIPATION_VALUE] > 0 else Constants.CONCILIATION_OPTION_MOVEMENT

def createColumnConciliacao(data):

  columnConciliacao = data.apply(verifyConciliacao, axis=1)

  return columnConciliacao

def verifyMl(data): 
  return data[Constants.DATA_KEY_ML_COMMISSION] if data[Constants.DATA_KEY_PAYMENT_WAY] == Constants.PAYMENT_WAY_TRANSFERENCIA else data[Constants.DATA_KEY_ML_COMMISSION]

def verifyValorBruto(data): 
  return data[Constants.DATA_KEY_NET_VALUE] if data[Constants.DATA_KEY_PAYMENT_WAY] == Constants.PAYMENT_WAY_TRANSFERENCIA else data[Constants.DATA_KEY_GROSS_AMOUNT]

def calcPorcentegeValue(value, total):
  return round((value/total) * 100, 2)

def printDataFrame(data):
  print(data[[
  Constants.DATA_KEY_TRANSACTION_DATE,
  Constants.DATA_KEY_ID_SELLER,
  Constants.DATA_KEY_PAYMENT_WAY, 
  Constants.DATA_KEY_ML_COMMISSION,
  Constants.DATA_KEY_GROSS_AMOUNT,
  Constants.DATA_KEY_COMMISSION,
  Constants.DATA_KEY_CONCILIATION,
  ]].head())

def printConciliacao(data, numberOfRows):
  # Calculando o número de conciliação
  infoConciliados = dataSheets[Constants.DATA_KEY_CONCILIATION] == Constants.CONCILIATION_OPTION_CONCILIATED
  infoNumeroConciliados = dataSheets[infoConciliados].shape[0]
  infoPorcentageConciliados = calcPorcentegeValue(infoNumeroConciliados, numberOfRows)

  # Calculando o número de não conciliação
  infoNotConciliados = dataSheets[Constants.DATA_KEY_CONCILIATION] == Constants.CONCILIATION_OPTION_NOT_CONCILIATED
  infoNumeroNotConciliados = dataSheets[infoNotConciliados].shape[0]
  infoPorcentageNotConciliados = calcPorcentegeValue(infoNumeroNotConciliados, numberOfRows)

  # Calculando o número de Retiradas
  infoRetirada = dataSheets[Constants.DATA_KEY_CONCILIATION] == Constants.CONCILIATION_OPTION_WITHDRAWAL
  infoNumeroRetirada = dataSheets[infoRetirada].shape[0]
  infoPorcentageRetirada = calcPorcentegeValue(infoNumeroRetirada, numberOfRows)

  # Calculando o número de Movitações
  infoMovimentacao = dataSheets[Constants.DATA_KEY_CONCILIATION] == Constants.CONCILIATION_OPTION_MOVEMENT
  infoNumeroMovimentacao = dataSheets[infoMovimentacao].shape[0]
  infoPorcentageMovimentacao = calcPorcentegeValue(infoNumeroMovimentacao, numberOfRows)

  print('\nNúmero de ocorrências coluna Conciliação:')
  print(
  f'Conciliados - {infoNumeroConciliados} - {infoPorcentageConciliados}% ' + 
  f'| Não Conciliados - {infoNumeroNotConciliados} - {infoPorcentageNotConciliados}% ' + 
  f'| Retiradas - {infoNumeroRetirada} -  {infoPorcentageRetirada}% ' + 
  f'| Movimentações - {infoNumeroMovimentacao} - {infoPorcentageMovimentacao}% '
  )

def printPaymentWays(data, numberOfRows):
  # Calculando o número de Boleto
  infoPaymentWayBoleto = dataSheets[Constants.DATA_KEY_PAYMENT_WAY] == Constants.PAYMENT_WAY_BOLETO
  infoPaymentWayNumeroBoleto = dataSheets[infoPaymentWayBoleto].shape[0]
  infoPaymentWayPorcentageBoleto = calcPorcentegeValue(infoPaymentWayNumeroBoleto, numberOfRows)

  # Calculando o número de Cartão de Crédito
  infoPaymentWayCard = dataSheets[Constants.DATA_KEY_PAYMENT_WAY] == Constants.PAYMENT_WAY_CARD
  infoPaymentWayNumeroCard = dataSheets[infoPaymentWayCard].shape[0]
  infoPaymentWayPorcentageCard = calcPorcentegeValue(infoPaymentWayNumeroCard, numberOfRows)

  # Calculando o número de Estorno
  infoPaymentWayEstorno = dataSheets[Constants.DATA_KEY_PAYMENT_WAY] == Constants.PAYMENT_WAY_ESTORNO
  infoPaymentWayNumeroEstorno = dataSheets[infoPaymentWayEstorno].shape[0]
  infoPaymentWayPorcentageEstorno = calcPorcentegeValue(infoPaymentWayNumeroEstorno, numberOfRows)

  # Calculando o número de Transferência
  infoPaymentWayTransferencia = dataSheets[Constants.DATA_KEY_PAYMENT_WAY] == Constants.PAYMENT_WAY_TRANSFERENCIA
  infoPaymentWayNumeroTransferencia = dataSheets[infoPaymentWayTransferencia].shape[0]
  infoPaymentWayPorcentageTransferencia = calcPorcentegeValue(infoPaymentWayNumeroTransferencia, numberOfRows)

  print('\nNúmero de ocorrências coluna Método de pagamento:')
  print(
  f'Boleto - {infoPaymentWayNumeroBoleto} - {infoPaymentWayPorcentageBoleto}% ' + 
  f'| Cartão de Crédito - {infoPaymentWayNumeroCard} - {infoPaymentWayPorcentageCard}% ' + 
  f'| Estorno - {infoPaymentWayNumeroEstorno} - {infoPaymentWayPorcentageEstorno}% ' + 
  f'| Transferência - {infoPaymentWayNumeroTransferencia} - {infoPaymentWayPorcentageTransferencia}% '
  )

def printInfo(data): 
  print('\n__Info__')

  numberOfRows = len(dataSheets)
  print(f'Número total de linhas: {numberOfRows}')

  printConciliacao(data, numberOfRows)
  printPaymentWays(data, numberOfRows)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Import and read excel database
data = pd.read_excel(Constants.DATA_PATH)
dataSheets = pd.DataFrame(data).fillna(0)

# Building column Conciliação
dataSheets[Constants.DATA_KEY_CONCILIATION] = createColumnConciliacao(dataSheets)

# Update columns "Comissão ML por parcela" and "Valor bruto da parcela"
dataSheets[Constants.DATA_KEY_ML_COMMISSION] = dataSheets.apply(verifyMl, axis=1)
dataSheets[Constants.DATA_KEY_GROSS_AMOUNT] = dataSheets.apply(verifyValorBruto, axis=1)

# Print informations to the user
printDataFrame(dataSheets)
printInfo(dataSheets)