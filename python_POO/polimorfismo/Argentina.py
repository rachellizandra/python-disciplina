class Argentina: 
    def capital(self):
        print('Buenos Aires é a capital da Argentina.')
    
    def lingua_oficial(self):
        print('O espanhol é a língua oficial da Argentina.')

class Brasil:
    def capital(self):
        print('Brasília é a capital do Brasil.')

    def lingua_oficial(self):
        print('O português é a língua oficial do Brasil.')

brasil = Brasil()
argentina = Argentina()

for pais in (brasil, argentina):
    pais.capital()
    pais.lingua_oficial