from datetime import datetime, timezone, timedelta, date
import conexa_quarta, conexa_quinta, conexa_sexta

def dia_da_semana():
    timezone_offset = -3.0
    tzinfo = timezone(timedelta(hours=timezone_offset))
    dia = datetime.now(tzinfo).strftime("%d")
    dia = int(dia)
    mes = datetime.now(tzinfo).strftime("%m")
    mes = int(mes)
    ano = datetime.now(tzinfo).strftime("%Y")
    ano = int(ano)
    data = date(year=ano, month=mes, day=dia)
    week_day = data.isoweekday()
    return week_day

week_day = dia_da_semana()

if week_day == 3:
    conexa_quarta.delete_wednesday()

if week_day == 4:
    conexa_quinta.navigate_thursday()

if week_day == 5:
    conexa_sexta.navigate_friday()