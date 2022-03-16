class aluno:
    def __init__ (self,nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.media = 0.0
        self.nota2 = nota2
    
    def media_geral(self):
        notas = 0
        notas = self.nota1 + self.nota2
        self.media = notas/2
        return self.media
    
    def mostrar_dados(self):
        print(self.nome, self.nota1, self.nota2, self.media) 
    
    def resultado(self):
        if(self.media >= 6.0):
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")
            
aluno1 = aluno('jose',6.0,4.0)
aluno1.media_geral()
aluno1.resultado()