import json

class Persistencia:
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
    
    def salvar(self, dados):
        with open(self.arquivo, 'w') as f:
            json.dump(dados, f, indent=4)
    
    def abrir(self):
        try:
            with open(self.arquivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
