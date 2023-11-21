# Execução do Projeto

## Pré-requisitos
- Docker instalado

## Passos para Execução
1. Clone este repositório.
2. Certifique-se de ter o Docker instalado.
3. No terminal, navegue até o diretório do projeto.
4. Execute o comando: 

    docker-compose up -d

## Isso iniciará o container do MongoDB.
5. Instale as dependências Python:

    pip install -r requirements.txt
51. Se usar anaconda ou conda dê o seguinte comando:

    conda install pymongo

6. Execute o script Python para interagir com o MongoDB:

python atividade4.py

7. Após executar derrube o container do MongoDB

docker-compose down

## Isso derrubará o container do MongoDB.# A4_BD_Massivos



Primeiro print de execução: 

![image](https://github.com/natansr/A4_BD_Massivos/assets/4833993/d61e9935-b659-42f5-bac8-e2d7b1784770)
