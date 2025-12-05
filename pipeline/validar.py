import pandas as pd
import pandera as pa
from pandera import Column, Check, DataFrameSchema


def criar_schema():

    schema = DataFrameSchema({

        # cliente_id — inteiro, não nulo, único
        "cliente_id": Column(int, nullable=False, unique=True),

        # idade — inteiro entre 18 e 80
        "idade": Column(int, Check.in_range(18, 80)),

        # renda_mensal — float entre 1000 e 50000
        "renda_mensal": Column(float, Check.in_range(1000, 50000)),

        # já existente
        "tempo_conta_meses": Column(int, Check.in_range(1, 240)),
        "num_produtos": Column(int, Check.in_range(1, 5)),
        "tem_cartao_credito": Column(int, Check.isin([0, 1])),

        # score_credito — float entre 300 e 850
        "score_credito": Column(float, Check.in_range(300, 850)),

        # respondeu_campanha — target: 0 ou 1
        "respondeu_campanha": Column(int, Check.isin([0, 1])),
    })

    return schema


def validar_dados(df):

    schema = criar_schema()

    print("Validando dados...")

    try:
        df_validado = schema.validate(df)
        print("✅ Dados válidos!")
        return df_validado
    except pa.errors.SchemaError as e:
        print("❌ Dados inválidos!")
        print(f"Erro: {e}")
        raise


if __name__ == "__main__":
    df = pd.read_csv("../data/clientes_campanha.csv")

    try:
        df_validado = validar_dados(df)
        print(f"\n{len(df_validado)} registros validados com sucesso!")
    except Exception as e:
        print(f"\nFalha na validação. Verifique os TODOs!")