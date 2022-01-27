import smtplib
from datetime import datetime


def replacing(string_para_salvar):
    st = string_para_salvar.replace("é", "e")
    st = st.replace("É", "E")
    st = st.replace("é", "e")
    st = st.replace("Ã", "A")
    st = st.replace("Â", "A")
    st = st.replace("â", "a")
    st = st.replace("Á", "A")
    st = st.replace("á", "a")
    st = st.replace("ã", "a")
    st = st.replace("Õ", "O")
    st = st.replace("Ô", "O")
    st = st.replace("Ó", "O")
    st = st.replace("õ", "o")
    st = st.replace("ô", "o")
    st = st.replace("ó", "o")
    st = st.replace("ê", "e")
    st = st.replace("Ê", "E")
    st = st.replace("Í", "I")
    st = st.replace("í", "i")
    st = st.replace("ç", "c")
    st = st.replace("Ç", "C")
    return st


def sendmail(message, email):
    #print("email: ", message)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('seu-email-configurado-para-envio@gmail.com', 'senha_do_seu_mensageiro')
    dia = datetime.now().strftime("%d")
    dia = int(dia)
    dia = dia + 1
    dia = str(dia)
    mes = datetime.now().strftime("%m")
    mes = str(mes)
    ano = datetime.now().strftime("%Y")
    ano = str(ano)
    data = str(dia + "." + mes + "." + ano)
    subject = str("Agenda Conexa Saude - %s" % (data))
    body_non_ascii = f"O erro na agenda da conexa saude e: {message}"
    body_encoded = body_non_ascii.encode("ascii", "ignore")
    body = body_encoded.decode()
    msg = str(subject + "\n\n\n" + body)
    server.sendmail(
        'seu-email-configurado-para-envio@gmail.com',
        email,
        msg
    )
    print("email enviado")
    server.quit()
