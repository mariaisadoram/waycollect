from django import forms
from main.models import Local

class LocalForm(forms.ModelForm):
    class Meta:
        model=Local
        fields='__all__'
        widgets={
            'nome_local':forms.TextInput(attrs={'class':'form-control','placeholder':'Nome do estabelecimento'}),
            'cidade':forms.TextInput(attrs={'class':'form-control','placeholder':'Cidade'}),
            'uf':forms.TextInput(attrs={'class':'form-control','placeholder':'UF'}),
            'cep':forms.TextInput(attrs={'class':'form-control','placeholder':'CEP'}),
            'rua':forms.TextInput(attrs={'class':'form-control','placeholder':'Endereço'}),
            'num_residencial':forms.NumberInput(attrs={'class':'form-control','placeholder':'Número'}),
            'bairro':forms.TextInput(attrs={'class':'form-control','placeholder':'Bairro'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email para contato'}),
            'fone':forms.TextInput(attrs={'class':'form-control','placeholder':'Telefone para contato'}),
            'nome_responsavel':forms.TextInput(attrs={'class':'form-control','placeholder':'Nome do responsável'}),
            'cpf_responsavel':forms.TextInput(attrs={'class':'form-control','placeholder':'CPF do responsável', 'id':'cpf'}),
            'disponibilidade':forms.Textarea(attrs={'class':'form-control','style':'height: 150px;','placeholder':'Informe às pessoas quais os dias da semana e os horários específicos em que vocês estarão disponíveis para o recolhimento.\nEXEMPLOS:\n1. Estamos abertos de Segunda ao Sábado, das 07:00 às 12:00 e das 14:00 às 19:00.\n2. Estamos abertos de Segunda à Sexta, das 07:00 às 12:00 e das 14:00 às 19:00. E aos Sábados, das 07:00 às 12:00.'}),
            'imagem':forms.FileInput(attrs={'class':'form-control-file'})
        }
