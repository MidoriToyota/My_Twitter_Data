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
import numpy as np


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

    '''Faça a análise dos dados do seu Twitter de um jeito fácil e sem precisar instalar nada!'''

    '''O `My Twitter Data` é um aplicativo criado para que qualquer pessoa com uma conta no twitter
    consiga analisar seus próprios dados de perfil sem a necessidade de baixar e instalar programas em seu computador.
    É tudo online e para começar basta completar alguns passos.
    '''

    '''Confira noso vídeo demonstrativo:'''

    st.video('https://youtu.be/1HhTusjL42k')

    '''Para uma explicação mais detalhada, clique em  `passo a passo` no **Menu Inicial** à esquerda.'''


# Página de Informações
def info_page():

    st.title('Passo a passo')

    st.header('**1. Obter dados do Twitter**')

    '''
    Para solicitar seus dados do Twitter, basta fazer o seguinte:
    - Entre no site do [Twitter](https://twitter.com/home) e no menu à esquerda acesse a opção `Mais`
    - Clique na opção `Conta`, vá em **Dados e permissões** e clique em `Seus dados do Twitter`
    - Vá em **Baixar seus dados do Twitter**, insira sua senha e clique em `Confirmar`
    - Na opção **Twitter**, clique em `Solicitar arquivo`

    Ficou confuso? Confira o vídeo explicativo:
    '''

    st.video('https://youtu.be/1HhTusjL42k')

    '''
    O Twitter irá preparar os seus dados e os enviará por e-mail assim que eles estiverem prontos!
    Depois disso você pode seguir para o passo número 2.
    '''

    st.header('**2. Converter dados json para csv**')

    '''
    Inicialmente, quando solicitávamos nossos os dados ao Twitter, ele  fornecia um arquvivo csv com as informações de todos os tweetes pessoais.
    Arquivos nesse formato são de fácil leitura e interpretação, sendo os mais utilizados em análise de dados. 
    Há algum tempo, entretanto, a rede social deixo de fornecer os dados nesse formato e passou a fornecer no formato json (.js).
    Esse tipo de arquivo é muito poluído, não sendo possível analisar utilizando métodos convencionais. Sendo assim, precisamos convertê-lo para csv!
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
    Se tudo deu certo até aqui, podemos seguir para o último passo: ANALISAR
    '''

    st.header('**3. Analisar os dados**')

    '''
    Se você já está com seu arquivo csv em mãos, chegou a hora de se divertir!
    '''
    '''
    No **Menu Inicial** à esquerda clique em `Iniciar análise` e faça o upload do seus arquivo csv.
    '''
    '''
    Confira com a gente tudo o que é possível fazer com o My Twitter Data:
    '''
    st.video('https://youtu.be/1HhTusjL42k')

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
                                         'Word Cloud'))
        if analysis == 'Visão geral':
            analysis_1(df)
        if analysis == 'Análise temporal':
            analysis_2(df)
        if analysis == 'Word Cloud':
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

    st.header('**Tweets com mais retweets**')
    max_retweet = max(df.retweet_count)
    st.table(df['full_text'][df['retweet_count'] == max_retweet])

    st.header('**Tweets mais curtidos**')
    max_favorite = max(df.favorite_count)
    st.table(df['full_text'][df['favorite_count'] == max_favorite])

    st.header('**Quantidade de curtidas recebidas**')
    graph_favorite(df)

    st.header('**Quantidade retweets recebidos**')
    graph_retweet(df)



# Análise temporal (Análise 2)
def analysis_2(df):

    sns.set_style("darkgrid")

    st.header('**Escolha o período de análise**')
    df = slider_period(df)

    st.header('**Nº de tweets no período**')
    graph_period(df)

    st.header('**Total de tweets por mês**')
    graph_month(df)

    st.header('**Total de tweets por dia da semana**')
    graph_weekday(df)

    st.header('**Total de tweets por ano**')
    graph_year(df)



# Análise 3
def analysis_3(df):

    st.header('**Remoção de palavras**')
    words = stopwords_general(df)
    words = stopwords_user(words)

    st.header('**Nuvem de palavras**')
    try: 
        graph_wordcloud(words)
    except:
        st.info('Não foi possível carregar a Word Cloud')

    st.header('**Palavras mais frequentes**')
    graph_freq(words)


## Funções complementares ## --------------------------------------------------------------------------------------

# Função de Pré processamento
def preprocess(df):

    get_datetime = lambda x: datetime.strptime(x, '%a %b %d %H:%M:%S %z %Y')
    get_weekday = lambda date: calendar.day_name[date.weekday()]
    get_month = lambda date: calendar.month_name[date.month]
    get_hour = lambda date: date.hour
    get_year = lambda date: date.year
    get_date = lambda d: d.date
    get_favorite = lambda f: 'Com like' if f > 0 else 'Sem like'
    get_retweet = lambda r: 'Com retweet' if r > 0 else 'Sem retweet'

    df['created_at'] = df.created_at.apply(get_datetime)
    df['weekday'] = df.created_at.apply(get_weekday)
    df['month'] = df.created_at.apply(get_month)
    df['hour'] = df.created_at.apply(get_hour)
    df['year'] = df.created_at.apply(get_year)
    df['date'] = df.created_at.apply(get_date)
    df['favorite'] = df.favorite_count.apply(get_favorite)
    df['retweet'] = df.retweet_count.apply(get_retweet)

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

    range_date = st.date_input("Insira o período de início e fim que deseja analisar no formato (YYYY/MM/DD - YYYY/MM/DD)", [min_date, max_date])

    try:
        df_subset = df[(df['date']>= range_date[0]) & (df['date']<= range_date[1])]
        
        if st.button('Resetar período'):
            return df
        else:
            return df_subset

    except:
        st.error('Inisira um período válido no formato YYYY/MM/DD – YYYY/MM/DD')
        return df

def stopwords_general(df):

    raw_tweets = []
    for tweets in df['full_text']:
        raw_tweets.append(tweets)

    raw_string = ''.join(raw_tweets)
    no_links = re.sub(r'http\S+', '', raw_string)
    #no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_links)
    #no_special_characters = re.sub('[^A-Za-z ]+', '', no_links)

    with open('stopwords-pt.txt', 'r', encoding="utf-8") as file:
        words_list = file.read().replace('\n', ',')
    STOPWORDS = words_list.split(",")

    words = no_links.split(" ")
    words = [w for w in words if len(w) > 2]  # Ignorar artigos a, o, as, os, um...
    words = [w.lower() for w in words]
    words = [w for w in words if w not in STOPWORDS]

    with open('stopwords-extra.txt', 'r', encoding="utf-8") as file:
        words_list_extra = file.read().replace('\n', ',')

        STOPWORDS_extra = words_list_extra.split(",")

    words = [w for w in words if w not in STOPWORDS_extra]

    return words


def graph_freq(words):
    df_palavras = FreqDist(words)
    fig = plt.figure(figsize=(10,5))
    df_palavras.plot(20, cumulative=False)
    st.pyplot()


def stopwords_user(words):
    words_list_user = st.text_input('Insira todas as palavras que deseja remover da Word Cloud (separadas por vírgula e sem espaço entre as vírgulas)', 'ainda,vou')
    STOPWORDS_user = words_list_user.split(",")
    words_new = [w for w in words if w not in STOPWORDS_user]

    options = st.multiselect(
        'Palavras removidas',
        STOPWORDS_user,
        STOPWORDS_user)

    return words_new
    
def graph_wordcloud(words):
    from wordcloud import WordCloud
    wordcloud = WordCloud(background_color="white", width = 1000, height = 500, scale=1).generate(' '.join(words))
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot()

def graph_favorite(df):
    df_favorite = Counter(df.favorite)
    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))

    labels = list(df_favorite.keys()) 
    values = list(df_favorite.values())

    wedges, texts = ax.pie(values, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
            bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate("{} ({})".format(labels[i], values[i]), xy=(x, y), xytext=(0.9*np.sign(x), 0.9*y),
                    horizontalalignment=horizontalalignment, **kw)

    st.pyplot()

def graph_retweet(df):

    df_retweet = Counter(df.retweet)

    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))

    labels = list(df_retweet.keys()) 
    values = list(df_retweet.values())

    wedges, texts = ax.pie(values, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
            bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate("{} ({})".format(labels[i], values[i]), xy=(x, y), xytext=(0.9*np.sign(x), 0.9*y),
                    horizontalalignment=horizontalalignment, **kw)

    st.pyplot()

## Execução ## --------------------------------------------------------------------------------------
 

menu()
