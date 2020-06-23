# Pacotes ----------------------------------------------------------------------------------------------

import streamlit as st
import webbrowser
import pandas as pd
import seaborn as sns
from datetime import datetime
from datetime import date
import calendar
import matplotlib.pyplot as plt
from collections import Counter
from streamlit import caching
import time
import re
from nltk import tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from wordcloud import WordCloud



## Menu Sidebar ## --------------------------------------------------------------------------------------

def menu():
    st.sidebar.header('**Menu Inicial**')

    page = st.sidebar.radio("", ('My Twitter Data',
                                'Passo a passo', 'Iniciar análise'))

    if page == 'My Twitter Data':
        about()
    if page == 'Passo a passo':
        info_page()
    if page == 'Iniciar análise':
        analysis_page()



## Páginas principais ## --------------------------------------------------------------------------------

# Sobre o My Twitter Data
def about():

    st.title('My Twitter Data')

    '''Faça a análise dos dados do seu Twitter de um jeito fácil sem instalar nada!'''

    '''O `My Twitter Data` é um aplicativo criado para que qualquer pessoa com uma conta no twitter
    consiga analisar seus próprios dados de perfil sem a necessidade de instalar programas em seu computador.
    É tudo online e para começar basta completar alguns passos.
    '''

    '''Confira noso vídeo explicativo:'''

    st.video('https://youtu.be/1HhTusjL42k')


# Página de Informações
def info_page():

    st.title('Passo a passo')

    st.header('**1. Obter dados do Twitter**')

    '''
    Para fazer a solicitação, basta fazer o seguinte:
    - Entre no site do [Twitter](https://twitter.com/home) e no Menu à esquerda acesse a opção `Mais`
    - Clique na opção `Conta`, vá em **Dados e permissões** e clique em `Seus dados do Twitter`
    - Vá em **Baixar seus dados do Twitter**, insira sua senha e clique em `Confirmar`
    - Na opção **Twitter**, clique em `Solicitar arquivo`

    Se fizer tudo correto, você irá chegar na seguinte janela:
    '''

    st.image('solicitar_arquivo.jpg')

    '''
    Pronto! O Twitter irá preparar os seus dados e te enviará por e-mail assim que eles estiverem prontos!
    Depois disso você pode seguir para o próximo passo: Converter o arquivo tweets.js para um formato legível.
    '''

    st.header('**2. Converter dados json para csv**')

    '''
    Inicialmente, quando solicitávamos os dados do Twitter, ele  fornecia um arquvivo csv com as informações de todos os tweetes pessoais.
    Há algum tempo, entretanto, a rede social deixo de fornecer os dados no formato csv e passou a fornecer no formato json (.js).
    Esse tipo de formato não serve para se realizar análises e, portanto, precisamos convertê-lo para csv.
    '''

    '''
    Para a nossa felicidade o site http://tweetjstocsv.glitch.me/ já faz todo esse trabalho pesado. Para fazer a conversão do arquivo, basta seguir os seguintes passos:
    - Faça o download dos dados enviados por e-mail pelo Twitter.
    - Descompacte o arquivo.
    - Acesse o [site](http://tweetjstocsv.glitch.me/) para realizar a conversão dos dados.
    - Dentro do site, clique em `Choose your tweets.js`
    - Para encontrar o arquivo, entre na pasta **data** e procure por `tweets.js`.
    - Selecione o arquivo e clique em `Abrir`
    - Espere alguns segundos para que seus dados sejam convertidos
    - Clique no botão `Save .csv` e faça o download dos seus arquivos
    '''

    '''
    Agora só falta fazer o upload dos seus dados no `My Twitter Data` para gerar uma análise personalizada dos seus tweets!
    '''


# Página de análise
def analysis_page():
    st.sidebar.header('**Upload dos dados**')

    uploaded_file = st.sidebar.file_uploader("", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = preprocess(df)

        st.sidebar.header('**Tipo de análise**')
        analysis = st.sidebar.radio("", ('Visão geral',
                                         'Análise temporal',
                                         'Nuvem de palavras'))
        if analysis == 'Visão geral':
            analysis_1(df)
        if analysis == 'Análise temporal':
            analysis_2(df)
        if analysis == 'Nuvem de palavras':
            analysis_3(df)



## Análises ## --------------------------------------------------------------------------------------


# Análise Geral (Análise 1)
def analysis_1(df):

    st.header('**Estatísticas básicas**')
    st.write('Nº total de tweets: ',len(df))
    st.write('Nº total de retweets recebidos: ', sum(df.retweet_count))
    st.write('Nº total de likes recebidos: ', sum(df.favorite_count))
    st.write('Dia do primeiro tweet enviado: ', min(df.date))
    st.write('Dia do último tweet enviado: ', max(df.date))
    

    st.header('**Tweets mais curtidos**')
    max_favorite = max(df.favorite_count)
    st.table(df['full_text'][df['favorite_count'] == max_favorite])



# Análise temporal (Análise 2)
def analysis_2(df):

    sns.set_style("darkgrid")

    st.header('**Escolha o período de análise**')
    df = slider_period(df)

    st.header('**Nº de tweets no período**')
    graph_period(df)

    st.header('**Total de tweets por mês**')
    graph_month(df)

    st.header('**Total tweets por dia da semana**')
    graph_weekday(df)

    st.header('**Total de tweets por ano**')
    graph_year(df)



# Análise 3
def analysis_3(df):
    st.header('**Palavras mais frequentes**')
    graph_freq(df)


## Funções complementares ## --------------------------------------------------------------------------------------

# Função de Pré processamento
def preprocess(df):

    get_datetime = lambda x: datetime.strptime(x, '%a %b %d %H:%M:%S %z %Y')
    get_weekday = lambda date: calendar.day_name[date.weekday()]
    get_month = lambda date: calendar.month_name[date.month]
    get_hour = lambda date: date.hour
    get_year = lambda date: date.year
    get_date = lambda d: d.date

    df['created_at'] = df.created_at.apply(get_datetime)
    df['weekday'] = df.created_at.apply(get_weekday)
    df['month'] = df.created_at.apply(get_month)
    df['hour'] = df.created_at.apply(get_hour)
    df['year'] = df.created_at.apply(get_year)
    df['date'] = df.created_at.apply(get_date)

    return df

# Gráfico tweets no período
def graph_period(df):

    # Preparação do período
    df_range = pd.DataFrame({'date': []})
    df_range["date"] = df["date"].astype("datetime64")
    df_range = df_range.groupby([df_range["date"].dt.year, df_range["date"].dt.month]).count()

    # Tweets por período
    n_range = range(len(df_range))
    plt.figure(figsize = (10,5))
    ax = plt.subplot()
    ax.set_xticks(n_range)
    ax.set_xticklabels(df_range.index, rotation = 35)
    plt.plot(n_range, df_range['date'].values)
    plt.xlabel('Mês e ano')
    plt.ylabel('Quantidade de tweets')
    st.pyplot()

def graph_month(df):
    df_month = Counter(df.month)
    print(df_month)
    desired_order_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_month = {k: df_month[k] for k in desired_order_list}

    n_month = range(len(df_month))
    plt.figure(figsize = (10,5))
    ax = plt.subplot()
    ax.set_xticks(n_month)
    ax.set_xticklabels(df_month.keys(), rotation = 40)
    plt.bar(n_month, df_month.values())
    plt.title('Nº de tweets por mês')
    plt.xlabel('Mês')
    plt.ylabel('Quantidade de tweets')
    st.pyplot()

# Gráfico Tweets por dia da semana
def graph_weekday(df):


    df_weekday = Counter(df.weekday)
    desired_order_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    df_weekday = {k: df_weekday[k] for k in desired_order_list}
    n_weekday = range(len(df_weekday))

    plt.figure(figsize=(10, 5))
    ax = plt.subplot()
    ax.set_xticks(n_weekday)
    ax.set_xticklabels(df_weekday.keys(), rotation=30)
    plt.bar(n_weekday, df_weekday.values())
    plt.xlabel('Dia da semana')
    plt.ylabel('Quantidade de tweets')
    st.pyplot()



# Gráfico tweets por ano
def graph_year(df):
    df_year = Counter(df.year)
    desired_order_list = sorted(df_year)
    df_year = {k: df_year[k] for k in desired_order_list}

    n_year = range(len(df_year))
    plt.figure(figsize = (10,5))
    ax = plt.subplot()
    ax.set_xticks(n_year)
    ax.set_xticklabels(df_year.keys())
    plt.bar(n_year, df_year.values())
    plt.xlabel('Ano')
    plt.ylabel('Quantidade de tweets')
    st.pyplot()


def slider_period(df):

    min_date = min(df.date)
    max_date = max(df.date)

    range_date = st.date_input("Insira o período inicial e final das análises", [min_date, max_date])

    try:
        df_subset = df[(df['date']>= range_date[0]) & (df['date']<= range_date[1])]
        
        if st.button('Resetar período'):
            return df
        else:
            return df_subset

    except:
        st.error('Inisira um período válido no formato YYYY/MM/DD – YYYY/MM/DD')
        return df

def graph_freq(df):

    raw_tweets = []
    for tweets in df['full_text']:
        raw_tweets.append(tweets)

    raw_string = ''.join(raw_tweets)
    no_links = re.sub(r'http\S+', '', raw_string)
    no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_links)
    no_special_characters = re.sub('[^A-Za-z ]+', '', no_unicode)
    with open('stopwords-pt.txt', 'r', encoding="utf-8") as file:
        stop_word = file.read().replace('\n', ',')
    STOPWORDS = stop_word.split(",")

    words = no_special_characters.split(" ")
    words = [w for w in words if len(w) > 2]  # Ignorar artigos a, o, as, os, um...
    words = [w.lower() for w in words]
    words = [w for w in words if w not in STOPWORDS]

    words_extra = ['pra', 'voc', 'acho', 'ficar', 'vou', 'deram', 'mim', 'vocs', 'vamos', 'algum','est', 'fazendo', 'tava', 'fica', 'ento', 'pro']

    with open("stopwords-extra.txt", "w") as output:
        for item in words_extra:
            output.write(str(item) + "\n")

    with open('stopwords-extra.txt', 'r', encoding="utf-8") as file:
        stop_word = file.read().replace('\n', ',')

        STOPWORDS_extra = stop_word.split(",")

    words = [w for w in words if w not in STOPWORDS_extra]

    df_palavras = FreqDist(words)
    fig = plt.figure(figsize=(10,5))
    df_palavras.plot(20, cumulative=False)
    st.pyplot()


## Execução ## --------------------------------------------------------------------------------------
 
menu()
