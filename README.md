# Projeto de Machine Learning com Scikit-Learn

Este projeto cria um modelo de machine learning para prever a qualidade do vinho utilizando o conjunto de dados de vinhos. Utilizamos a biblioteca Scikit-Learn para treinar e avaliar o modelo.

## Estrutura do Projeto

machine-learning/
│
├── data/
│   └── winequality-red.csv
│
├── src/
│   └── wine_quality.py
│
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt


## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/machine-learning.git
   cd machine-learning

2.  Construa a imagem Docker:
    docker build -t machine-learning .

3.  Execute o contêiner Docker:
    docker run -v $(pwd)/data:/app/data machine-learning
    