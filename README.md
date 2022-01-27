# Conexa Saude Same Day Scheduller Blocker

Conjunto de Scripts para capacitar ao Conexa Saúde a possibilidade de bloquear novos agendamentos dentro do dia corrente.

Está configurado para executar em servidores *headless*. Porém, já possui a codificação comentada para execução com Webdriver em um PC.

Personalizado, configurado e implantado, esse script permite que, de forma automática, o aplicativo da Conexa Saúde, utilizado pela Unimed Porto Alegre para teleconsulta, ganhe a função de bloquear agendamentos para o mesmo dia. 

Observação: infelizmente, da maneira como o Conexa Saúde foi pobremente desenvolvido, há uma limitação importante: durante o dia da semana em que se está bloqueando o agendamento, também os clientes ficam impossibilitados de agendarem para as semanas seguintes naquele mesmo dia da semana. Transcorrido aquele dia, novamente ficam liberados os agendamentos para datas futuras.

