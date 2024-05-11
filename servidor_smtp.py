import smtplib

servidor_email = smtplib.smtp('smtp.gmail.com',58)

print(servidor_email.starttls()) 

servidor_email.login("",PAradoxo22$?) 

remetente = ''
destinatarios = [gleisson.batista@prozeducacao.com.br]
conteudo = oi! eu sou bom pra cacete,genial,o cruzeiro e o maior de minas e logo vai ser o maior do mundo,humildade e caráter sempre.
servidor_email.Sendmail(remetente,destinatario,conteudo)
servidor_email.quit()