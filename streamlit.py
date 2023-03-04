import openai
import json
import os
import streamlit as st

openai.api_key = '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'

modelo = "text-davinci-002"

def gerar_recomendacao(gostei, n_gostei):
    resposta = openai.Completion.create(
        engine=modelo,
        prompt=f"Considerando que eu gosto dos filmes {gostei} e não gosto dos filmes {n_gostei}, me recomende um filme do meu gosto. Quero que a resposta seja em portugues e venha no formato de dicionário python, contendo o nome do filme, a nota do imdb, uma sinopse, imagem do cartaz e o motivo do filme ser recomendado.",
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
        presence_penalty=0,
        frequency_penalty=0,
    )

    dict_resposta = json.loads(resposta.choices[0].text.replace(".\n\n","").replace("'", '"'))

    return dict_resposta

st.title("Recomendações de filmes")

gostei = st.multiselect("Quais filmes você gostou?", ["Interstelar", "Capitão Fantástico", "Batman", "Superman"])
n_gostei = st.multiselect("Quais filmes você não gostou?", ["Harry Potter", "O Enigma de Outro Mundo", "Senhor dos Anéis"])

if st.button("Gerar recomendação"):
    if not gostei or not n_gostei:
        st.warning("Selecione pelo menos um filme que você gostou e um que você não gostou.")
    else:
        recomendacao = gerar_recomendacao(gostei, n_gostei)
        st.write(f"Recomendação: {recomendacao['nome_do_filme']}")
        st.write(f"Nota do IMDb: {recomendacao['nota_imdb']}")
        st.write(f"Sinopse: {recomendacao['sinopse']}")
        st.image(recomendacao['imagem_do_cartaz'], caption="Cartaz do filme recomendado")
        st.write(f"Motivo da recomendação: {recomendacao['motivo']}")