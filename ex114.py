import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu Erro!')
else:
    print('Tudo OK!')
    print(site.read())