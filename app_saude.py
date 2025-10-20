# -*- coding: utf-8 -*-

# ==========================================
# 🧠 ACOMPANHAMENTO DE SAÚDE – DATA ROBOT
# ==========================================
# Etapa 1: Registro e visualização de dados
# ==========================================

# 1️⃣ Importação das bibliotecas básicas
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# ==========================================
# 2️⃣ Estrutura inicial dos DataFrames
# ==========================================

# Criar tabelas vazias (você pode preencher manualmente ou importar CSV depois)
atividades = pd.DataFrame(columns=["data", "hora", "atividade", "duração_min", "intensidade", "observações"])
medicamentos = pd.DataFrame(columns=["data", "hora", "medicamento", "dose", "observações"])
humor = pd.DataFrame(columns=["data", "hora", "nível_humor", "observações"])
observacoes = pd.DataFrame(columns=["data", "hora", "anotação"])
nutricao = pd.DataFrame(columns=["data", "hora", "refeição", "calorias", "glicemia", "insulina", "observações"])

# ==========================================
# 3️⃣ Funções para inserção manual
# ==========================================

def registrar_atividade(atividade, duração_min, intensidade, observações=""):
    try:    global atividades
    agora = dt.datetime.now()
    novo = pd.DataFrame([{
        "data": agora.date(),
        "hora": agora.strftime("%H:%M"),
        "atividade": atividade,
        "duração_min": duração_min,
        "intensidade": intensidade,
        "observações": observações
    }])
    atividades = pd.concat([atividades, novo], ignore_index=True)
        print("✅ Atividade registrada com sucesso!")
    except Exception as e:        print(f'Erro ao registrar: {e}')
def registrar_medicamento(medicamento, dose, observações=""):
    try:    global medicamentos
    agora = dt.datetime.now()
    novo = pd.DataFrame([{
        "data": agora.date(),
        "hora": agora.strftime("%H:%M"),
        "medicamento": medicamento,
        "dose": dose,
        "observações": observações
    }])
    medicamentos = pd.concat([medicamentos, novo], ignore_index=True)
    print("💊 Registro de medicamento adicionado!")

def registrar_humor(nível_humor, observações=""):
    try:    global humor
    agora = dt.datetime.now()
    novo = pd.DataFrame([{
        "data": agora.date(),
        "hora": agora.strftime("%H:%M"),
        "nível_humor": nível_humor,
        "observações": observações
    }])
    humor = pd.concat([humor, novo], ignore_index=True)
    print("🙂 Registro de humor adicionado!")

def registrar_observacao(anotação):
    try:    global observacoes
    agora = dt.datetime.now()
    novo = pd.DataFrame([{
        "data": agora.date(),
        "hora": agora.strftime("%H:%M"),
        "anotação": anotação
    }])
    observacoes = pd.concat([observacoes, novo], ignore_index=True)
        print("📝 Observação registrada!")
    except Exception as e:        print(f'Erro ao registrar: {e}')
def registrar_refeicao(refeição, calorias, glicemia=None, insulina=None, observações=""):
    try:    global nutricao
    agora = dt.datetime.now()
    novo = pd.DataFrame([{
        "data": agora.date(),
        "hora": agora.strftime("%H:%M"),
        "refeição": refeição,
        "calorias": calorias,
        "glicemia": glicemia,
        "insulina": insulina,
        "observações": observações
    }])
    nutricao = pd.concat([nutricao, novo], ignore_index=True)
        print("🍽️ Refeição registrada!")
    except Exception as e:        print(f'Erro ao registrar: {e}')
# ==========================================
# 4️⃣ Funções para importar dados de planilhas CSV
# ==========================================

def importar_dados(nome_arquivo, tipo):
    global atividades, medicamentos, humor, observacoes, nutricao
    df = pd.read_csv(nome_arquivo)
    if tipo == "atividades":
        atividades = pd.concat([atividades, df], ignore_index=True)
    elif tipo == "medicamentos":
        medicamentos = pd.concat([medicamentos, df], ignore_index=True)
    elif tipo == "humor":
        humor = pd.concat([humor, df], ignore_index=True)
    elif tipo == "observacoes":
        observacoes = pd.concat([observacoes, df], ignore_index=True)
    elif tipo == "nutricao":
        nutricao = pd.concat([nutricao, df], ignore_index=True)
    print(f"📂 Dados de {tipo} importados com sucesso!")

# ==========================================
# 5️⃣ Visualização e métricas diárias
# ==========================================

def ver_resumo(dia=None):
    if dia is None:
        dia = dt.date.today()

    print(f"\n📅 Resumo do dia: {dia}")
    print("\nAtividades:")
    print(atividades[atividades["data"] == pd.to_datetime(dia)])

    print("\nMedicamentos:")
    print(medicamentos[medicamentos["data"] == pd.to_datetime(dia)])

    print("\nRefeições:")
    print(nutricao[nutricao["data"] == pd.to_datetime(dia)])

    print("\nHumor:")
    print(humor[humor["data"] == pd.to_datetime(dia)])

def ver_graficos(dia=None):
    if dia is None:
        dia = dt.date.today()
    dados = nutricao[nutricao["data"] == pd.to_datetime(dia)]

    if not dados.empty:
        plt.figure(figsize=(8,4))
        plt.bar(dados["refeição"], dados["calorias"])
        plt.title(f"🍽️ Calorias por refeição ({dia})")
        plt.ylabel("Calorias (kcal)")
        plt.show()
    else:
        print("Nenhum dado nutricional disponível para este dia.")

registrar_atividade("Caminhada", 45, "moderada")
registrar_medicamento("Insulina basal", "8U")
registrar_refeicao("Café da manhã", 250, glicemia=110, insulina=1)
registrar_humor(4, "Acordei disposta!")
registrar_observacao("Glicemia estável durante a manhã")

ver_resumo()

ver_graficos()

importar_dados("nutricao.csv", "nutricao")

# ==========================================
# 🩺 ETAPA 2 – PAINEL INTERATIVO E DASHBOARD
# ==========================================

import ipywidgets as widgets
from IPython.display import display, clear_output

# ==========================================
# 🧾 1️⃣ Formulários Interativos
# ==========================================

def painel_registro():
    """
    Exibe formulários interativos para registrar atividades, medicamentos,
    humor, observações e refeições.
    """

    print("📋 Painel de Registro de Dados de Saúde")

    aba = widgets.ToggleButtons(
        options=["Atividades", "Medicamentos", "Humor", "Observações", "Nutrição"],
        description="Escolha:",
        button_style=""
    )

    out = widgets.Output()

    def mostrar_form(change):
        out.clear_output()
        with out:
            if change["new"] == "Atividades":
                form_atividade()
            elif change["new"] == "Medicamentos":
                form_medicamento()
            elif change["new"] == "Humor":
                form_humor()
            elif change["new"] == "Observações":
                form_observacao()
            elif change["new"] == "Nutrição":
                form_refeicao()

    aba.observe(mostrar_form, names="value")
    display(aba, out)
    mostrar_form({"new": "Atividades"})

# ==========================================
# 🏃‍♀️ 2️⃣ Funções dos formulários
# ==========================================

def form_atividade():
    atividade = widgets.Text(description="Atividade:")
    duracao = widgets.IntText(description="Duração (min):")
    intensidade = widgets.Dropdown(options=["leve", "moderada", "intensa"], description="Intensidade:")
    obs = widgets.Text(description="Obs:")
    btn = widgets.Button(description="Salvar", button_style="success")

    def salvar(b):
        registrar_atividade(atividade.value, duracao.value, intensidade.value, obs.value)
        clear_output()
            print("✅ Atividade registrada!\n")
    except Exception as e:        print(f'Erro ao registrar: {e}')        painel_registro()

    display(atividade, duracao, intensidade, obs, btn)
    btn.on_click(salvar)

def form_medicamento():
    medicamento = widgets.Text(description="Medicamento:")
    dose = widgets.Text(description="Dose:")
    obs = widgets.Text(description="Obs:")
    btn = widgets.Button(description="Salvar", button_style="success")

    def salvar(b):
        registrar_medicamento(medicamento.value, dose.value, obs.value)
        clear_output()
        print("💊 Medicamento registrado!\n")
        painel_registro()

    display(medicamento, dose, obs, btn)
    btn.on_click(salvar)

def form_humor():
    nivel = widgets.IntSlider(value=3, min=1, max=5, step=1, description="Humor (1-5):")
    obs = widgets.Text(description="Obs:")
    btn = widgets.Button(description="Salvar", button_style="success")

    def salvar(b):
        registrar_humor(nivel.value, obs.value)
        clear_output()
        print("🙂 Humor registrado!\n")
        painel_registro()

    display(nivel, obs, btn)
    btn.on_click(salvar)

def form_observacao():
    anot = widgets.Textarea(description="Anotação:")
    btn = widgets.Button(description="Salvar", button_style="success")

    def salvar(b):
        registrar_observacao(anot.value)
        clear_output()
        print("📝 Observação salva!\n")
        painel_registro()

    display(anot, btn)
    btn.on_click(salvar)

def form_refeicao():
    refeicao = widgets.Dropdown(options=["Café da manhã", "Lanche", "Almoço", "Jantar"], description="Refeição:")
    calorias = widgets.FloatText(description="Calorias:")
    glicemia = widgets.FloatText(description="Glicemia:")
    insulina = widgets.FloatText(description="Insulina:")
    obs = widgets.Text(description="Obs:")
    btn = widgets.Button(description="Salvar", button_style="success")

    def salvar(b):
        registrar_refeicao(refeicao.value, calorias.value, glicemia.value, insulina.value, obs.value)
        clear_output()
            print("🍽️ Refeição registrada!\n")
    except Exception as e:        print(f'Erro ao registrar: {e}')        painel_registro()

    display(refeicao, calorias, glicemia, insulina, obs, btn)
    btn.on_click(salvar)

# ==========================================
# 📊 3️⃣ Painel de visualização de métricas
# ==========================================

def painel_metrico():
    data = widgets.DatePicker(description="Data:", value=pd.Timestamp.today())
    btn = widgets.Button(description="Ver resumo", button_style="info")
    out = widgets.Output()

    def mostrar(b):
        out.clear_output()
        with out:
            ver_resumo(data.value)
            ver_graficos(data.value.date())

    display(data, btn, out)
    btn.on_click(mostrar)

# ==========================================
# 🚀 4️⃣ Painel principal
# ==========================================

def painel_principal():
    print("🌿 Bem-vinda ao seu painel de saúde!")
    escolha = widgets.ToggleButtons(
        options=["Registrar Dados", "Ver Métricas"],
        description="Ação:"
    )
    out = widgets.Output()

    def mudar_painel(change):
        out.clear_output()
        with out:
            if change["new"] == "Registrar Dados":
                painel_registro()
            elif change["new"] == "Ver Métricas":
                painel_metrico()

    escolha.observe(mudar_painel, names="value")
    display(escolha, out)

# ==========================================
# 🧩 Executar painel principal
# ==========================================

painel_principal()


# ==========================================
# 🩺 ACOMPANHAMENTO DE SAÚDE - APP STREAMLIT
# ==========================================

import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# ==========================================
# 1️⃣ Inicialização dos DataFrames
# ==========================================

def inicializar_dados():
    if "atividades" not in st.session_state:
        st.session_state["atividades"] = pd.DataFrame(columns=["data", "hora", "atividade", "duração_min", "intensidade", "observações"])
    if "medicamentos" not in st.session_state:
        st.session_state["medicamentos"] = pd.DataFrame(columns=["data", "hora", "medicamento", "dose", "observações"])
    if "humor" not in st.session_state:
        st.session_state["humor"] = pd.DataFrame(columns=["data", "hora", "nível_humor", "observações"])
    if "observacoes" not in st.session_state:
        st.session_state["observacoes"] = pd.DataFrame(columns=["data", "hora", "anotação"])
    if "nutricao" not in st.session_state:
        st.session_state["nutricao"] = pd.DataFrame(columns=["data", "hora", "refeição", "calorias", "glicemia", "insulina", "observações"])

# ==========================================
# 2️⃣ Funções de registro
# ==========================================

def registrar(df_name, dados):
    agora = dt.datetime.now()
    dados["data"] = agora.date()
    dados["hora"] = agora.strftime("%H:%M")
    st.session_state[df_name] = pd.concat([st.session_state[df_name], pd.DataFrame([dados])], ignore_index=True)

# ==========================================
# 3️⃣ Interface de registro
# ==========================================

def tela_registro():
    st.header("📋 Registro de Dados de Saúde")
    aba = st.tabs(["🏃‍♀️ Atividades", "💊 Medicamentos", "🙂 Humor", "📝 Observações", "🍽️ Nutrição"])

    # Atividades
    with aba[0]:
        atividade = st.text_input("Atividade:")
        duracao = st.number_input("Duração (min):", min_value=0, step=1)
        intensidade = st.selectbox("Intensidade:", ["leve", "moderada", "intensa"])
        obs = st.text_input("Observações:")
        if st.button("Salvar atividade"):
            registrar("atividades", {"atividade": atividade, "duração_min": duracao, "intensidade": intensidade, "observações": obs})
            st.success("✅ Atividade registrada com sucesso!")

    # Medicamentos
    with aba[1]:
        medicamento = st.text_input("Medicamento:")
        dose = st.text_input("Dose:")
        obs = st.text_input("Observações:", key="obs_med")
        if st.button("Salvar medicamento"):
            registrar("medicamentos", {"medicamento": medicamento, "dose": dose, "observações": obs})
            st.success("💊 Medicamento registrado!")

    # Humor
    with aba[2]:
        nivel = st.slider("Nível de humor (1-5):", 1, 5, 3)
        obs = st.text_input("Observações:", key="obs_humor")
        if st.button("Salvar humor"):
            registrar("humor", {"nível_humor": nivel, "observações": obs})
            st.success("🙂 Humor registrado!")

    # Observações
    with aba[3]:
        anot = st.text_area("Anotação:")
        if st.button("Salvar observação"):
            registrar("observacoes", {"anotação": anot})
            st.success("📝 Observação registrada!")

    # Nutrição
    with aba[4]:
        refeicao = st.selectbox("Refeição:", ["Café da manhã", "Lanche", "Almoço", "Jantar"])
        calorias = st.number_input("Calorias (kcal):", min_value=0, step=10)
        glicemia = st.number_input("Glicemia (mg/dL):", min_value=0, step=1)
        insulina = st.number_input("Insulina (U):", min_value=0.0, step=0.5)
        obs = st.text_input("Observações:", key="obs_nutri")
        if st.button("Salvar refeição"):
            registrar("nutricao", {"refeição": refeicao, "calorias": calorias, "glicemia": glicemia, "insulina": insulina, "observações": obs})
            st.success("🍽️ Refeição registrada!")

# ==========================================
# 4️⃣ Tela de visualização e métricas
# ==========================================

def tela_metricas():
    st.header("📊 Visualização e Métricas")
    data = st.date_input("Selecione a data:", dt.date.today())

    # Filtrar dados do dia
    atividades = st.session_state["atividades"]
    medicamentos = st.session_state["medicamentos"]
    humor = st.session_state["humor"]
    nutricao = st.session_state["nutricao"]

    st.subheader("🏃‍♀️ Atividades")
    st.dataframe(atividades[atividades["data"] == data])

    st.subheader("💊 Medicamentos")
    st.dataframe(medicamentos[medicamentos["data"] == data])

    st.subheader("🙂 Humor")
    st.dataframe(humor[humor["data"] == data])

    st.subheader("🍽️ Nutrição")
    dados_dia = nutricao[nutricao["data"] == data]
    st.dataframe(dados_dia)

    if not dados_dia.empty:
        fig, ax = plt.subplots()
        ax.bar(dados_dia["refeição"], dados_dia["calorias"])
        ax.set_title("Calorias por refeição")
        st.pyplot(fig)

        media_glicemia = dados_dia["glicemia"].mean()
        total_calorias = dados_dia["calorias"].sum()
        total_insulina = dados_dia["insulina"].sum()

        st.markdown(f"""
        **Resumo do dia ({data}):**
        - 🔥 Calorias totais: **{total_calorias:.0f} kcal**
        - 💉 Insulina total: **{total_insulina:.1f} U**
        - 🩸 Glicemia média: **{media_glicemia:.0f} mg/dL**
        """)

# ==========================================
# 5️⃣ Execução principal
# ==========================================

def main():
    st.set_page_config(page_title="Acompanhamento de Saúde", page_icon="💙", layout="centered")
    st.title("🌿 Acompanhamento de Saúde Pessoal")

    inicializar_dados()

    menu = st.sidebar.radio("Menu", ["Registrar dados", "Ver métricas"])

    if menu == "Registrar dados":
        tela_registro()
    else:
        tela_metricas()

if __name__ == "__main__":
    main()
