import openai
import json
import os
import streamlit as st
import streamlit.components.v1 as components

openai.api_key = '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'

modelo = "text-davinci-002"

def gerar_recomendacao(gostei):
    resposta = openai.Completion.create(
        engine=modelo,
        prompt=f"Considerando que eu assisti e gostei dos filmes {gostei}, me recomende um filme pouco conhecido que eu vá gostar e ainda não assisti. Quero que a resposta seja em portugues e venha no formato de dicionário python, contendo o nome do filme, a nota do imdb, uma sinopse, link de uma imagem do filme no google e o motivo do filme ser recomendado.",
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.6,
        presence_penalty=0.8,
        frequency_penalty=0.3,
    )

    dict_resposta = json.loads('{"nome"'+resposta.choices[0].text.replace("'",'"').split('"nome"')[1].replace("\n",''))

    return dict_resposta

st.title("Recomendações de filmes")

gostei = st.multiselect(f"Quais filmes você gostou?", ["O Poderoso Chefão",
    "O Senhor dos Anéis: O Retorno do Rei",
    "Forrest Gump: O Contador de Histórias",
    "Star Wars: Episódio V - O Império Contra-Ataca",
    "O Rei Leão",
    "Os Caçadores da Arca Perdida",
    "De Volta para o Futuro",
    "Clube da Luta",
    "Matrix",
    "Pulp Fiction: Tempo de Violência",
    "A Lista de Schindler",
    "Batman: O Cavaleiro das Trevas",
    "Os Suspeitos",
    "O Labirinto do Fauno",
    "Cidade de Deus"])

col1, col2 = st.columns([1, 2])

def icon_text(text):
    components.html(f'<i class="fa-brands fa-imdb"></i> {text}', height=30)


if st.button("Gerar recomendação"):
    if not gostei:
        st.warning("Selecione pelo menos um filme que você gostou e um que você não gostou.")
    else:
        recomendacao = gerar_recomendacao(gostei)
        col1.image(list(recomendacao.values())[3], caption="Cartaz do filme recomendado")
        col2.write(f"Você provávelmente gostará de: **{list(recomendacao.values())[0]}**")
        col2.write(f"**Nota do IMDb:** {list(recomendacao.values())[1]}")
        #col2.write(icon_text('teste'))
        col2.write(f"**Sinopse:** {list(recomendacao.values())[2]}")
        col2.write(f"**Motivo da recomendação:** {list(recomendacao.values())[4]}")