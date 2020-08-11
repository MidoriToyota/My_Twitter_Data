# My Twitter Data

**_Web App com Streamlit e Plotly :_** https://mytwitterdata.herokuapp.com/

Faça a análise dos dados do seu Twitter de um jeito fácil e sem precisar instalar nada!

O My Twitter Data é um aplicativo criado para que qualquer pessoa com uma conta no twitter consiga analisar seus próprios dados sem a necessidade de baixar e instalar programas em seu computador. O app foi desenvolvido em python utilizando o pacote Streamlit para gerar o layout e Plotly para cria os gráficos iterativos.

<h3 align="center"><br>
  <a href="https://youtu.be/Cvcr_I27w8Q"><img src="https://github.com/MidoriToyota/My_Twitter_Data/blob/master/img/video.jpg" alt="Video demonstrativo" width="600px" />
  </a><br><br>
</h3>

## Rodando o app localmente

Para instalar o My Twitter Data e rodar localmente na sua máquina, siga o passo à passo abaixo:

```bash
# Download do repositório
git clone https://github.com/MidoriToyota/My_Twitter_Data.git

# Instalar os pacotes do requirements.txt
pip install -r requirements.txt

# Rodar o app
streamlit run my_twitter_data.py
```

## Funcionalidades

**_Principais Estatísticas_**

No app você pode ver as suas principais estatísticas como: nº total de tweets, curtidas, retweets, qual foi o tweet mais curtido ou o mais retweetado.

<h3 align="center">
  <img src="https://github.com/MidoriToyota/My_Twitter_Data/blob/master/img/estatisticas.jpg" alt="Principais estatísticas" width="600px" />
  <br><br>
</h3>

<h3 align="center">
  <img src="https://github.com/MidoriToyota/My_Twitter_Data/blob/master/img/donut.jpg" alt="Gráfico Pizza" width="600px" />
  <br><br>
</h3>

**_Análise temporal_**

Você também pode fazer uma análise temporal para entender, por exemplo, quais os meses, dias da semana ou horários que você mais posta tweets.
Isso tudo de acordo com o período de análise que você delimitar.

<h3 align="center">
  <img src="https://github.com/MidoriToyota/My_Twitter_Data/blob/master/img/periodo1.jpg" alt="Período de análise" width="600px" />
  <br><br>
</h3>

<h3 align="center">
  <img src="https://github.com/MidoriToyota/My_Twitter_Data/blob/master/img/periodo2.jpg" alt="Período de análise" width="600px" />
  <br><br>
</h3>

<h3 align="center">
  <img src="https://github.com/MidoriToyota/My_Twitter_Data/blob/master/img/periodo3.jpg" alt="Período de análise" width="600px" />
  <br><br>
</h3>

<h3 align="center">
  <img src="https://github.com/MidoriToyota/My_Twitter_Data/blob/master/img/periodo4.jpg" alt="Período de análise" width="600px" />
  <br><br>
</h3>


**_Word Cloud_**

Com a Word Cloud você consegue visualizar quais suas palavras mais frequêntes. Se houver alguma palavra que não faz sentido
na sua núvem, basta removê-la digitando-a na caixa de remoção.

<h3 align="center">
  <img src="https://github.com/MidoriToyota/My_Twitter_Data/blob/master/img/wordcloud1.jpg" alt="Nuvem de palavras" width="600px" />
  <br><br>
</h3>

<h3 align="center">
  <img src="https://github.com/MidoriToyota/My_Twitter_Data/blob/master/img/wordcloud2.jpg" alt="Nuvem de palavras" width="600px" />
  <br><br>
</h3>
