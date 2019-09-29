# Password Storage

Atividade prática desenvolvida em Python para a disciplina de Estratégia e Inteligência Cibernética. Seu principal objetivo é o armazenamento seguro de senhas utilizando criptografia simétrica e hashs.

## Pré-Requisitos
1. Sistema Operacional Linux;
2. Python 3.*.

## Instalação:
1. Clone esse projeto e entre no repositório;
2. Execute o comando abaixo para instalação de dependências:

```
pip install -r requirements.txt
```

3. Execute o arquivo main, com o comando:

```
python main.py
```

4. Digite a Master Key;
5. Com o menu principal sendo exibido, selecione a opção: "0. Reset/First Use" e siga as instruções para a inserção do primeiro registro.


## Funcionamento:

### Master Key:
Definição:

É utilizada pelo algoritmo para criptografar e descriptografar a tabela onde serão armazenados todos os registros. Ela é transformada em um hash via SHA256, utilizando como SALT o Mac Address da máquina. Esse Hash será utilizado como chave para a criptografia via AES dos registros que serão salvos em um arquivo chamado _ciphertext.bin_.

Exemplo:
```
A-bpjp64D_PvgJiJtiS50plnYaaZlNXB8X7YMpMfQGo=
```
### Tabela Formatada:
Definição:

Formatação para visualização da Tabela Bruta utilizando a biblioteca [tabulate](https://pypi.org/project/tabulate/).

Exemplo:

```
App       User                 Password    Note
--------  -------------------  ----------  -----------
Gmail     mail@gmail.com       5nyVpYkf
Twitter   Us3r                 &G4lp%r5    Mail: mail2@gmail.com
Caixa     4130268696111251     841481      Token: 7589
```

### Tabela Bruta:
Definição:

Como o algoritmo manipula a tabela, é utilizado somente uma string. O divisor de colunas é "[nc]" e o divisor de linhas "[nl]", separando assim, um registro do outro.

```
app + "[nc]" + user + "[nc]" + pw + "[nc]" + note + "[nl]"
```

Exemplo: 

```
"Twitter[nc]mail@gmail.com[nc]&G4lp%r5[nc]Mail: mail2@gmail.com[nl]"
```

### Tabela Criptografada:
Definição:

A tabela criptografada é salva como _ciphertext.bin_, utilizando a biblioteca de [Fernet (symmetric encryption)](https://cryptography.io/en/latest/fernet/). 
Fernet foi construído utilizando premissas de criptografia padrão. Especificamente, ele usa:
* AES no modo CBC com uma chave de 128 bits para criptografia;
* PKCS7 para o padding;
* HMAC usando SHA256 para autenticação;
* Os vetores de inicialização são gerados usando os.urandom().

Para mais detalhes, consulte a [especificação técnica](https://github.com/fernet/spec/blob/master/Spec.md).

Exemplo: 

```
gAAAAABdkSM3HeVcC-jEVLQkw7NxUpefH1d7M2YlrQieK0hlltxhTlvpG9Q8HDXUPA80Vttr35jy3Dx-bEPDevw3rK49Ipty7v34GD8TeNrSQUh7TYWDUiJyGDRLCHxqOdGcwM28rKDZSsnBhxF1CN0ag39w9FFJnXk7v-s5WVD4tRjp9POPiOw=
```

## Menu:

### 1. Show Password Table
Exibe a tabela 

### 2. Search 

### 0. Reset/First Use

