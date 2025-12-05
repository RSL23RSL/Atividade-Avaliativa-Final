"""
Pipeline - Etapa 1: Carregar e Explorar Dados
"""
import pandas as pd

def carregar_dados(caminho):
    """
    Carrega o dataset de clientes.    Args:        caminho_arquivo: caminho para o CSV
        
    Returns:        DataFrame com os dados
    """
    # TODO 1: Use pd.read_csv() para carregar o arquivo
    # Dica: df = pd.read_csv(caminho_arquivo)
    

    df = pd.read_csv(caminho)
    print("")
    print("=" * 80) 
    print(f"Extraído: {len(df)} linhas de {caminho}")
    print("=" * 80)
    return df

def explorar_dados(df):
    """
    Mostra informações básicas sobre o dataset.
    Args:
        df: DataFrame a ser explorado
    """
    print("=" * 80)
    print("Exploração dos Dados")
    print("=" * 80)
    
    # TODO 2: Mostre o shape do DataFrame (linhas, colunas)
    print(f"Shape: {df.shape}\n")
        
    # TODO 3: Mostre os tipos de cada coluna
    print("Tipos de Cada Coluna:\n")
    print(df.dtypes)
    print("\n")
     # TODO 4: Mostre as 5 primeiras linhas
    print(df.head())
        
    print("=" * 80)


def verificar_target(df, coluna_target='respondeu_campanha'):
    """
    Verifica a distribuição da variável target.
        Args:
        df: DataFrame
        coluna_target: nome da coluna target
    """
    print("\nDISTRIBUIÇÃO DO TARGET EM NÚMEROS INTEIROS")
    print("-" * 80)
    
    # TODO 5: Mostre a contagem de cada valor do target
    # Dica: print(df[coluna_target].value_counts())
    print(df[coluna_target].value_counts())
    
    # TODO 6: Mostre a proporção (percentual) de cada valor
    # Dica: print(df[coluna_target].value_counts(normalize=True))
    print("\nDISTRIBUIÇÃO DO TARGET EM PERCENTUAL")
    print("-" * 80)
    print("proporção (percentual) de cada valor")
    print(df[coluna_target].value_counts(normalize=True))
    
    print("-" * 80)


# Teste local (executar este arquivo diretamente)
if __name__ == "__main__":
    df = carregar_dados("../data/clientes_campanha.csv")
    if df is not None:
        explorar_dados(df)
        verificar_target(df)
    else:
        print("ERRO: DataFrame não foi carregado. Complete o TODO 1!")
