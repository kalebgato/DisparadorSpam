import base64
 
def crypt(senha):
    cpt1 = senha
    cpt1_bytes = cpt1.encode('utf-8')
    b64 = base64.b64encode(cpt1_bytes)
    b64message = b64.decode('utf-8')
    return b64message

def dcrypt(hash):
    b64message = hash
    b64_bytes = b64message.encode('utf-8')
    m_bytes = base64.b64decode(b64_bytes)
    message = m_bytes.decode('utf-8')
    return message
