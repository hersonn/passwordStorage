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

É utilizada pelo algoritmo para criptografar e descriptografar a tabela onde serão armazenados todos os registros. Ela é transformada em um hash via SHA256 de 32 bytes, utilizando como SALT o Mac Address da máquina. Essa hash será utilizada como chave para criptografar via AES os registros que serão salvos em um arquivo chamado _ciphertext.bin_.

Exemplo:
```
xbH1db0Ul4jP__MS1Evd9qvzXJ8ve0tXZo5rpF-AmEk=
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
* SHA256 usando PBKDF2HMAC para derivação de chave;
* Vetores de inicialização são gerados via os.urandom().

Para mais detalhes, consulte a [especificação técnica](https://github.com/fernet/spec/blob/master/Spec.md).

Exemplo: 

```
gAAAAABdkSM3HeVcC-jEVLQkw7NxUpefH1d7M2YlrQieK0hlltxhTlvpG9Q8HDXUPA80Vttr35jy3Dx-bEPDevw3rK49Ipty7v34GD8TeNrSQUh7TYWDUiJyGDRLCHxqOdGcwM28rKDZSsnBhxF1CN0ag39w9FFJnXk7v-s5WVD4tRjp9POPiOw=
```

### Erro:
Descrição:

Caso a Master Key seja incorretamente inserida ou o algoritmo esteja sendo executado em outra máquina, qualquer operação resultará em erro. Em excessão à função "Reset/First Use" e "Dictionary Attack".

Exemplo:
```
cryptography.exceptions.InvalidSignature: Signature did not match digest.
During handling of the above exception, another exception occurred:
cryptography.fernet.InvalidToken
```
## Menu:

### 1. Show Password Table
Exibe a Tabela Formatada.

### 2. Search
Faz uma busca na tabela procurando por qualquer registro contendo a string de busca. Se mais de um registro conter a string, ambos serão exibidos.

### 3. Add Password
Adiciona um registro na tabela de senhas.

### 4. Edit Password
Faz uma busca na tabela procurando por qualquer registro contendo a string de busca. Se mais de um registro conter a string de busca, ambos serão removidos para a insersão do novo, portanto, busque por indentificadores únicos do registro a editar.

### 5. Remove Password
Faz uma busca na tabela procurando por qualquer registro contendo a string de busca. Se mais de um registro conter a string de busca, ambos serão removidos.

### 6. Master Key Hash
Exibe o hash da Master Key, já concatenada com o Mac Address.

### 7. Ciphertext
Exibe o conteúdo do arquivo _ciphertext.bin_.

### 8. Dictionary Attack
Faz um ataque de força bruta utilizando um dicionário das 10 milhões de senhas mais utilizadas. É utilizado os fluxos do próprio algoritmo para geração da HASH, facilitando o ataque.

### 9. Exit
Sair

### 0. Reset/First Use
No primeiro uso, é necessário que seja inserido ao menos um registro para que o arquivo _ciphertext.bin_ seja criado. Ele utilizará a Master Key que foi inserida na inicialização da sessão atual como chave de criptografia. Também pode ser usado como reinicialização do arquivo, excluindo todos os registros em caso de esquecimento da senha ou criação de uma nova tabela.
