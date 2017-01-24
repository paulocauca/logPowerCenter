logPowerCenter
==============


   Realiza a coleta do log da ULTIMA execução do workflow e imprime no terminal se chamado via shell.
O programa foi criado com objetivo de facilitar a verificação de erro no log do Power Center  sem ter conhecimento da ferramenta Monitor,
pois o mesmo converte os logs de binário para texto

### Demonstração

1. python show_log_powercenter.py DM_EXT_QUALIDADE W_QEN_DEFEITOS_ENCERRADOS

### Instalação

1. Faça o clone deste projeto com `git clone git@github.com:paulocauca/logPowerCenter.git`
2. Execute o código `python show_log_powercenter.py FOLDER WORKFLOW`


### Screenshot
1. Chamada via shell

![screen shot](https://github.com/paulocauca/logPowerCenter/blob/master/screen/sc1.PNG)

2. Chmando via aplicação Node.Js

![screen shot](https://github.com/paulocauca/logPowerCenter/blob/master/screen/sc2.PNG)

3. Filtrando erros ORA- e destacando para melhor visualização

![screen shot](https://github.com/paulocauca/logPowerCenter/blob/master/screen/sc3.PNG)