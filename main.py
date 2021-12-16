import configparser
import bin.coding



def frist_start():
    config_info = configparser.ConfigParser()
    config_info['DEFAULT'] = {
        "app": "Sistema de Envio Massivo de E-mail.",
        "topic" : "config File",
        "data" : 'data/data.db',
        }
    config_info['CONFIG_USER'] = {
        "host" : "",
        "port" : "",
        "user" : "",
        "pwd" : "",
        }
    with open('conf.ini', 'w') as fconf:
        config_info.write(fconf)

def host_config():
    config_info = configparser.ConfigParser()
    config_info.read('conf.ini')
    if (config_info['CONFIG_USER']['host'] == ""):
        print("(Caso não tenha esteja listado abaixo selecione 'PERSONALIZADO' e insira manualmente)")
        print("1 - Gmail")
        print("0 - Personalizado")
        host_sel = input("Selecione o seu provedor de Email (somente número): ")
        if host_sel == 0:
            config_info['CONFIG_USER']['host'] =  input("insira o Host:")
            config_info['CONFIG_USER']['port'] =  input("insira o numero da porta: ")
        if host_sel == 1:
            config_info['CONFIG_USER']['host'] = "smtp.gmail.com"
            config_info['CONFIG_USER']['port'] = 465
        with open('conf.ini', 'w') as fconf:
            config_info.write(fconf)
    print("SERVIDOR CONFIGURADO COM SUCESSO")
    
def config_user():
    config_info = configparser.ConfigParser()
    config_info.read('conf.ini')
  #  if (config_info['CONFIG_USER']['host'] == ""):
   #     host_config()
    if (config_info['CONFIG_USER']['user']=="") and (config_info['CONFIG_USER']['pwd']==""):
        email = input("Ensira seu email para login: ")
        paswd = input("Ensira sua senha: ")
        config_info['CONFIG_USER']['user'] = bin.coding.crypt(email)
        config_info['CONFIG_USER']['pwd'] = bin.coding.crypt(paswd)
        with open('conf.ini', 'w') as fconf:
                config_info.write(fconf)


frist_start()
host_config()
config_user()

