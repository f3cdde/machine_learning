import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import numpy as np

# Carregar o conjunto de dados
df = pd.read_csv('/app/data/winequality-red.csv', sep=';')

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Separar as características (X) e o alvo (y)
X = df.drop('quality', axis=1)
y = df['quality']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de RandomForest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia: {accuracy:.2f}')
print('Relatório de Classificação:')
print(classification_report(y_test, y_pred))

# Plotar a importância das características
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]
features = X.columns

plt.figure(figsize=(10, 6))
plt.title('Importância das Características')
plt.bar(range(X.shape[1]), importances[indices], align='center')
plt.xticks(range(X.shape[1]), features[indices], rotation=90)
plt.tight_layout()
plt.savefig('/app/data/feature_importance.png')
print("Gráfico salvo como 'feature_importance.png'")
