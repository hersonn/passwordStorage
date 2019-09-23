# Password Storage

Atividade prática desenvolvida em Python para a disciplina de Estratégia e Inteligência Cibernética.

## Pré-Requisitos:
1. Clone esse projeto e entre no repositório;
2. Execute o comando abaixo para instalação de dependências:

```
pip install -r requirements.txt
```

2. Execute a o arquivo main, com o comando:

```
py main.py
```

3. Digite sua primeira Senha;
4. Com o menu sendo exibido, selecione a opção: "0. Reset/First Use".


## Dicionário:
### Tabela Formatada:

```
App       User             Password    Note
--------  ---------------  ----------  -----------
Facebook  meu@mail.com     12345
Terra     meu@mail.com     123456      Token: 123
```

### Tabela Bruta:
Definição: 

```
app + "[nc]" + user + "[nc]" + pw + "[nc]" + note + "[nl]"
```

Exemplo: 

```
"Facebook[nc]meu@mail.com[nc]12345[nc]Token: 123[nl]"
```

### Tabela criptografada:
Exemplo: 

```
gAAAAABcdtoIdz7hv9UDaTUs8suGW7VDEGtE2dpctM6csUqnlbxp4sdpZjKj-Hhf8b31NW5Qk_WUlbO0LEDUdEkOkQHbSykph4osccqPNy-4RLs4-znIvjDEkklspuVFKYg5a3bQYePq9oYyrquSn8RF6a2QuQgDOi3Kz6H-mi3UjLydvjvWbx8=
```

## Menu:

### 1. Show Password Table
Exibe a tabela 

### 2. Search 

### 0. Reset/First Use
Importante: Ao alterar a variável salt, você NÃO conseguirá mais descriptografar os dados salvos (caso existam), após a alteração, é necessário utilizar a função: "0. Reset/First Use".
