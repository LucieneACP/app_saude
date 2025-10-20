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
     try:
     global atividades
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
     except Exception as e:
         print(f'Erro: {e}')

def registrar_medicamento(medicamento, dose, observações=""):
     try:
     global medicamentos
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
     except Exception as e:
         print(f'Erro: {e}')

def registrar_humor(nível_humor, observações=""):
     try:
     global humor
     agora = dt.datetime.now()
     novo = pd.DataFrame([{
     "data": agora.date(),
     "hora": agora.strftime("%H:%M"),
     "nível_humor": nível_humor,
     "observações": observações
     }])
     humor = pd.concat([humor, novo], ignore_index=True)
     print("🙂 Registro de humor adicionado!")
     except Exception as e:
         print(f'Erro: {e}')

def registrar_observacao(anotação):
     try:
     global observacoes
     agora = dt.datetime.now()
     novo = pd.DataFrame([{
     "data": agora.date(),
     "hora": agora.strftime("%H:%M"),
     "anotação": anotação
     }])
     observacoes = pd.concat([observacoes, novo], ignore_index=True)
     print("📝 Observação registrada!")
     except Exception as e:
         print(f'Erro: {e}')

def registrar_refeicao(refeição, calorias, glicemia=None, insulina=None, observações=""):
     try:
     global nutricao
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
     except Exception as e:
         print(f'Erro: {e}')

