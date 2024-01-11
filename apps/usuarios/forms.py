from django import forms

class LoginForm(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: joaosilva",
                "style": "min-width: 700px; width: 80%;",
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
            "class":"form-control",
            "placeholder":"Digite sua senha",
            "style": "min-width: 700px; width: 80%;",
            }
        )
    )

class CadastroForm(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: joaosilva",
                "style": "min-width: 700px; width: 80%;",
            }
        )
    )
    email=forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: joaosilva@xbto.com",
                "style": "min-width: 700px; width: 80%;",
            }
        )
    )
    senha_1=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
            "class":"form-control",
            "placeholder":"Digite sua senha",
            "style": "min-width: 700px; width: 80%;",
            }
        )
    )
    senha_2=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
            "class":"form-control",
            "placeholder":"Confirme sua senha",
            "style": "min-width: 700px; width: 80%;",
            }
        )
    )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError("Nome de usuário não pode conter espaços.")
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas não conferem.")
            else:
                return senha_2