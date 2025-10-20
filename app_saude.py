
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import streamlit as st

# Inicialização dos DataFrames
atividades = pd.DataFrame(columns=["data", "hora", "atividade", "duração_min", "intensidade", "observações"])
medicamentos = pd.DataFrame(columns=["data", "hora", "medicamento", "dose", "observações"])
humor = pd.DataFrame(columns=["data", "hora", "nível_humor", "observações"])
observacoes = pd.DataFrame(columns=["data", "hora", "anotação"])
nutricao = pd.DataFrame(columns=["data", "hora", "refeição", "calorias", "glicemia", "insulina", "observações"])

# Função genérica de registro
def registrar(df, dados):
    agora = dt.datetime.now()
    dados["data"] = agora.date()
    dados["hora"] = agora.strftime("%H:%M")
    return pd.concat([df, pd.DataFrame([dados])], ignore_index=True)

# Interface Streamlit
st.set_page_config(page_title="Saúde Pessoal", page_icon="💙", layout="centered")
st.title("🌿 Acompanhamento de Saúde")

aba = st.sidebar.radio("Menu", ["Registrar dados", "Ver métricas"])

if aba == "Registrar dados":
    st.header("📝 Registro de Dados")
    op = st.selectbox("Escolha o tipo de dado:", ["Atividade", "Medicamento", "Humor", "Observação", "Refeição"])

    if op == "Atividade":
        atividade = st.text_input("Atividade")
        duracao = st.number_input("Duração (min)", min_value=0)
        intensidade = st.selectbox("Intensidade", ["leve", "moderada", "intensa"])
        obs = st.text_input("Observações")
        if st.button("Salvar atividade"):
            atividades = registrar(atividades, {
                "atividade": atividade,
                "duração_min": duracao,
                "intensidade": intensidade,
                "observações": obs
            })
            st.success("✅ Atividade registrada!")

    elif op == "Medicamento":
        medicamento = st.text_input("Medicamento")
        dose = st.text_input("Dose")
        obs = st.text_input("Observações")
        if st.button("Salvar medicamento"):
            medicamentos = registrar(medicamentos, {
                "medicamento": medicamento,
                "dose": dose,
                "observações": obs
            })
            st.success("💊 Medicamento registrado!")

    elif op == "Humor":
        nivel = st.slider("Nível de humor (1-5)", 1, 5, 3)
        obs = st.text_input("Observações")
        if st.button("Salvar humor"):
            humor = registrar(humor, {
                "nível_humor": nivel,
                "observações": obs
            })
            st.success("🙂 Humor registrado!")

    elif op == "Observação":
        anot = st.text_area("Anotação")
        if st.button("Salvar observação"):
            observacoes = registrar(observacoes, {"anotação": anot})
            st.success("📝 Observação registrada!")

    elif op == "Refeição":
        refeicao = st.selectbox("Refeição", ["Café da manhã", "Lanche", "Almoço", "Jantar"])
        calorias = st.number_input("Calorias", min_value=0)
        glicemia = st.number_input("Glicemia", min_value=0)
        insulina = st.number_input("Insulina", min_value=0.0)
        obs = st.text_input("Observações")
        if st.button("Salvar refeição"):
            nutricao = registrar(nutricao, {
                "refeição": refeicao,
                "calorias": calorias,
                "glicemia": glicemia,
                "insulina": insulina,
                "observações": obs
            })
            st.success("🍽️ Refeição registrada!")

else:
    st.header("📊 Métricas do Dia")
    data = st.date_input("Selecione a data", dt.date.today())

    st.subheader("Atividades")
    st.dataframe(atividades[atividades["data"] == data])

    st.subheader("Medicamentos")
    st.dataframe(medicamentos[medicamentos["data"] == data])

    st.subheader("Humor")
    st.dataframe(humor[humor["data"] == data])

    st.subheader("Refeições")
    dados_dia = nutricao[nutricao["data"] == data]
    st.dataframe(dados_dia)

    if not dados_dia.empty:
        fig, ax = plt.subplots()
        ax.bar(dados_dia["refeição"], dados_dia["calorias"])
        ax.set_title("Calorias por refeição")
        st.pyplot(fig)

        st.markdown(f"""
        **Resumo Nutricional:**
        - 🔥 Calorias totais: **{dados_dia['calorias'].sum():.0f} kcal**
        - 💉 Insulina total: **{dados_dia['insulina'].sum():.1f} U**
        - 🧪 Glicemia média: **{dados_dia['glicemia'].mean():.0f} mg/dL**
        """)
