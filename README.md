**🌱 EcoGuard - Sistema De Monitoramento de Focos de Incêndios**

Bem-vindo ao EcoGuard! Este projeto foi desenvolvido para promover uma experiência intuitiva e fácil de gerenciar. Siga os passos abaixo para configurar e executar o projeto na sua máquina.

🛠️ Pré-requisitos
Antes de começar, certifique-se de ter instalado na sua máquina:

Python 3.8+
Pip

**📦 Instalação**

**Passo 1:** Baixar o projeto
Faça o download do arquivo ZIP clicando no botão Code > Download ZIP no repositório ou no link fornecido.
Extraia o conteúdo do ZIP para uma pasta de sua escolha.

**Passo 2:** Configurar o ambiente virtual
Abra o terminal na pasta extraída.
Crie um ambiente virtual executando o comando:
python -m venv venv
Ative o ambiente virtual:
Windows:
call venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

**Passo 3:** Instalar os requisitos
No terminal, execute o comando para instalar todas as dependências do projeto:

pip install -r requirements.txt


**⚙️ Configuração do Banco de Dados**
Após instalar as dependências, crie as migrações do banco de dados:
python manage.py makemigrations

**Aplique as migrações:**
python manage.py migrate

**🚀 Executar o Servidor**
Para iniciar o servidor local, rode o comando:
python manage.py runserver

Acesse o sistema no navegador pelo endereço:
http://127.0.0.1:8000/

📚 Resumo dos Comandos

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
call venv\Scripts\activate

# Ativar ambiente virtual (Mac/Linux)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Migrar banco de dados
python manage.py makemigrations
python manage.py migrate

# Rodar o servidor
python manage.py runserver
🤝 Contribuições
Sinta-se à vontade para contribuir com melhorias para o projeto! Abra uma issue ou envie um pull request com sua sugestão.

📝 Licença
Este projeto é distribuído sob a licença MIT.
