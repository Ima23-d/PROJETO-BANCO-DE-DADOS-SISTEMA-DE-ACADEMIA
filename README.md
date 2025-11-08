# 🏋️‍♂️ Sistema de Academia – Banco de Dados

**Projeto:** Sistema para Gestão de Academia  
**Autores:** Arthur Franco, Felipe Torres, Vinícius Nascimento  
**Instituição:** CESMAC  
**Repositório:** [Ima23-d/PROJETO-BANCO-DE-DADOS-SISTEMA-DE-ACADEMIA](https://github.com/Ima23-d/PROJETO-BANCO-DE-DADOS-SISTEMA-DE-ACADEMIA)

---

## 📘 Visão Geral

O **Sistema de Academia** é um projeto desenvolvido para gerenciar os dados e operações de uma academia.  
Ele permite o **cadastro e autenticação de alunos e personal trainers**, além de **gerenciar treinos personalizados** e informações físicas de cada aluno (peso, altura, nível, etc.).

O sistema foi construído utilizando **Python** e **banco de dados relacional (SQL)**, com uma estrutura modular para facilitar manutenção e expansão.

---

## ⚙️ Funcionalidades Principais

- 👤 **Cadastro de Alunos**
  - Nome, CPF, idade, peso, altura, e-mail, senha, nível e deficiência.
- 🔐 **Login de Aluno**
  - Autenticação via e-mail e senha.
- 💪 **Área do Aluno**
  - Visualização dos treinos criados pelo personal trainer.
  - Edição de dados pessoais (peso, altura, nível, etc.).
- 🧑‍🏫 **Área do Personal Trainer**
  - Cadastro e login de personal trainers.
  - Visualização dos alunos cadastrados.
  - Criação e atribuição de treinos para os alunos.
- 📊 **Banco de Dados Integrado**
  - Armazenamento de informações em tabelas SQL (Alunos, Personais, Treinos, etc.).
- 🧩 **Organização Modular**
  - Código separado em módulos: `Alunos`, `Personal`, `Query`, `config`.

---

## 🧱 Estrutura do Projeto
PROJETO-BANCO-DE-DADOS-SISTEMA-DE-ACADEMIA/
│
├── Alunos/
│ ├── cadastro_login.py
│ └── menu_aluno.py
│
├── Personal/
│ ├── cadastro_login.py
│ └── menu_personal.py
│
├── Query/
│ └── query.py
│
├── config/
│ └── config.py
│
├── main.py
├── requirements.txt
└── README.md


---

## 💾 Banco de Dados

O projeto utiliza um banco relacional **PostgreSQL** para armazenar as informações.

### Exemplo de Tabelas

#### 🧍‍♂️ Tabela: `alunos`
| Campo | Tipo | Descrição |
|-------|------|------------|
| id_aluno | SERIAL | Identificador único |
| nome_aluno | VARCHAR(100) | Nome completo |
| cpf | VARCHAR(14) | CPF do aluno |
| data_nascimento | DATE | Data de nascimento |
| idade | INT | Idade do aluno |
| peso | DECIMAL(5,2) | Peso corporal |
| gordura_corporal | DECIMAL(5,2) | Percentual de gordura |
| nivel | VARCHAR(20) | Básico, intermediário ou avançado |
| deficiencia | VARCHAR(100) | Tipo de deficiência (se houver) |
| email | VARCHAR(100) | E-mail para login |
| senha | VARCHAR(100) | Senha criptografada |

#### 🧑‍🏫 Tabela: `personais`
| Campo | Tipo | Descrição |
|-------|------|------------|
| id_personal | SERIAL | Identificador único |
| nome_personal | VARCHAR(100) | Nome completo |
| cpf | VARCHAR(14) | CPF do personal |
| especialidade | VARCHAR(100) | Área de atuação |
| email | VARCHAR(100) | E-mail para login |
| senha | VARCHAR(100) | Senha de acesso |

#### 💪 Tabela: `treinos`
| Campo | Tipo | Descrição |
|-------|------|------------|
| id_treino | SERIAL | Identificador único |
| id_aluno | INT | FK → alunos.id_aluno |
| id_personal | INT | FK → personais.id_personal |
| descricao | TEXT | Descrição do treino |
| data_criacao | DATE | Data de criação do treino |

---

## 🖥️ Telas e Menus

### 1. **Tela Inicial**
- Menu principal com as opções:
  - Login como Aluno
  - Login como Personal
  - Sair

### 2. **Cadastro de Aluno**
- Campos: Nome, CPF, Data de Nascimento, Idade, Peso, Altura, E-mail, Senha, Nível e Deficiência.

### 3. **Login de Aluno**
- Autenticação pelo e-mail e senha.
- Redirecionamento para o menu do aluno.

### 4. **Menu do Aluno**
- Opções:
  - Ver treinos
  - Atualizar informações
  - Voltar ao menu principal

### 5. **Login do Personal**
- Login de personal com e-mail e senha.
- Redirecionamento para o menu do personal.

### 6. **Menu do Personal**
- Opções:
  - Cadastrar novo aluno
  - Visualizar alunos cadastrados
  - Criar ou atribuir treinos
  - Voltar ao menu principal

---

## 📚 Bibliotecas Utilizadas

As bibliotecas estão listadas no arquivo `requirements.txt`.  
Abaixo estão as dependências principais utilizadas no projeto:

- **psycopg2** → Responsável pela conexão e execução de comandos SQL no banco de dados **PostgreSQL**.  
- **pwinput** → Utilizada para capturar senhas do usuário de forma oculta e segura no terminal (sem exibir os caracteres digitados).  
- **os** → Usada para interações com o sistema operacional, como limpar o terminal e manipular caminhos de arquivos.  
- **dotenv** → Carrega variáveis de ambiente a partir do arquivo `.env`, armazenando informações sensíveis como senhas e credenciais do banco de dados.  
- **bcrypt** → Biblioteca para **criptografia de senhas**, garantindo segurança no armazenamento e autenticação de usuários.  

> Instale todas as dependências com:
```bash
pip install -r requirements.txt

🚀 Instalação e Execução
Pré-requisitos

Python 3.8+

Banco de dados configurado (PostgreSQL)

Passos

Clone o repositório

git clone https://github.com/Ima23-d/PROJETO-BANCO-DE-DADOS-SISTEMA-DE-ACADEMIA.git
cd PROJETO-BANCO-DE-DADOS-SISTEMA-DE-ACADEMIA


Crie o ambiente virtual

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows


Instale as dependências

pip install -r requirements.txt


Configure o banco de dados

Edite o arquivo config/config.py com as credenciais corretas.

Execute os scripts SQL de criação das tabelas, se necessário.

Execute o sistema

python main.py


