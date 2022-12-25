from django.db import models
# from input_mask.widgets import InputMask


# Create your models here.

# class MyCustomInput(InputMask):
#    mask = {'cpf_responsavel' : '000.000.000-00', 'fone' : '(00)00000-0000', 'cep' : '00.000-000'} 

class Local(models.Model):
    nome_local = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    uf = models.CharField(max_length=10)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=100)
    num_residencial = models.IntegerField()
    cep = models.CharField(max_length=30)
    fone = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    nome_responsavel = models.CharField(max_length=150)
    cpf_responsavel = models.CharField(max_length=150)
    disponibilidade = models.TextField(max_length=800)
    # senha = models.CharField(max_length=100)
    imagem=models.ImageField(upload_to='pontos/',blank=True,null=True)

    def __str__(self) -> str:
        return self.nome_local


