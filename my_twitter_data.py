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
from unicodedata import normalize



## Menu Inicial ## --------------------------------------------------------------------------------------

# Sidebar principal
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

    # Sobre o My Twitter Data
    st.title('My Twitter Data')

    '''
    Faça a análise dos dados do seu Twitter de um jeito fácil e sem precisar instalar nada!

    O `My Twitter Data` é um aplicativo criado para que qualquer pessoa com uma conta no twitter
    consiga analisar seus próprios dados sem a necessidade de baixar e instalar programas em seu computador.
    É tudo online e para começar basta completar alguns passos.
  
    Confira nosso vídeo demonstrativo:
    '''

    st.video('https://youtu.be/1HhTusjL42k')

    '''Para uma explicação mais detalhada, clique em  `passo a passo` no **Menu Inicial** à esquerda.'''

    # Sobre o projeto
    st.title('Como surgiu')

    '''
    O `My Twitter Data` surgiu como um exercício para aplicar a linguagem python em análise de dados
    e utilizar o pacote streamlit para criar um aplicativo de análise online e iterativo. 

    A iniciativa surgiu após conhecer as funcionalidades do pacote streamlit no curso 

    Se deseja contribuir com o projeto, acesse o código fonte que se encontra no meu portfólio e faça um commit! 
    O `My Twitter Data` está aberto para sugestões de melhoria e críticas construtivas. 
    Segue o link do meu portifólio que contém o código fonte do projeto:

    https://midoritoyota.netlify.app/

    Aproveite para checar os outros projetos!
    '''

    # Sobre a autora
    st.title('Sobre a autora')

    '''
    Me chamo `Midori`, sou formada em Engenharia Civil e tenho 2 anos de experiência em obras (construção de edifícios). 
    Atualmente, estou em processo de transição de carreira para Ciência de Dados e realizo diversos projetos
    para botar em prática o que aprendo nos cursos que venho concluindo. Desenvolvi o `My Twitter Data` em python mas 
    minha linguagem principal é o R. Se quiser, você pode ver meus outros projetos acessando o meu portfolio pelo link:

    https://midoritoyota.netlify.app/

    Estou aberta a novas oportunidades. Se deseja me conhecer, me adicione no linkedin e vamos bater um papo!

    https://www.linkedin.com/in/midoritoyota/
    '''



# Página de Informações
def info_page():

    st.title('Passo a passo')

    # Obter os dados do Twitter
    st.header('**1. Solicite os dados ao Twitter**')
    '''
    Para solicitar seus dados do Twitter, basta fazer o seguinte:
    - Entre no site do [Twitter](https://twitter.com/home) e no menu à esquerda acesse a opção `Mais`
    - Clique na opção `Conta`, vá em **Dados e permissões** e clique em `Seus dados do Twitter`
    - Em **Baixar seus dados do Twitter**, insira sua senha e clique em `Confirmar`
    - Na opção **Twitter**, clique em `Solicitar arquivo`

    O Twitter irá preparar os seus dados e os enviará por e-mail assim que eles estiverem prontos.
    Depois disso você pode seguir para o passo número 2.
    '''
    # Converter dados json para csv
    st.header('**2. Converta os dados json para csv**')
    '''
    O arquivo fornecido pelo Twitter é em formato json e não conseguimos realizar análises com ele. 
    Para a nossa felicidade o site http://tweetjstocsv.glitch.me/ faz todo o trabalho pesado de converter o arquivo json para csv. 
    Para fazer a conversão do arquivo, basta seguir os seguintes passos:
    - Faça o download dos dados enviados por e-mail pelo Twitter.
    - Descompacte o arquivo.
    - Acesse o http://tweetjstocsv.glitch.me/ para realizar a conversão dos dados.
    - Dentro do site, clique em `Choose your tweets.js`
    - Para encontrar o arquivo, vá na pasta onde os dados foram descompactados.
    - Entre na pasta **data** e procure por `tweets.js`.
    - Selecione o arquivo e clique em `Abrir`
    - Espere alguns segundos para que seus dados sejam convertidos.
    - Clique no botão `Save .csv` e faça o download dos seus arquivos

    Se tudo deu certo até aqui, podemos seguir para o último passo: ANALISAR!
    '''

    # Analisar os daods
    st.header('**3. Analise os dados com o My Twitter Data**')
    '''
    Se você já está com seu arquivo csv em mãos, chegou a hora de se divertir!

    No **Menu Inicial** à esquerda clique em `Iniciar análise` e faça o upload do seu arquivo csv. 
    Depois basta escolher o tipo de análise que deseja realizar e modificar os parâmetros de visualização 
    acordo com a sua necessidade.

    Confira tudo o que é possível fazer com o My Twitter Data:
    '''
    st.video('https://youtu.be/1HhTusjL42k')

    # Não tenho dados
    st.header('**Não tenho dados pessoais do Twitter para usar**')
    '''
    Se você não usa o twitter ou não tem muitos dados para analisar, não tem problema! Você pode usar nossos dataset de exemplo clicando em Download:
    '''

    [Baixar arquivo]('https://drive.google.com/file/d/18LsOGWCJiJUVOevZdqWHJFm6GUrKL84d/view?usp=sharing')

    '''
    **Observação!**

    Os dados de exemplo foram coletados do Twitter de forma aleatória. Basicamente, utilizei a API do Twitter para 
    pegar os tweets de diversos usuários diferentes que haviam postado algo relacionado à "Ciência de Dados" no dia 23/06/2020. Como havia
    muito conteúdo desnecessário, fiz a substituição das palavras para que no final fosse gerada uma Word Cloud agradável. 
    Por esse motivo, o conteúdo dos tweets não fará sentido algum e tão pouco reflete à minha opinião sobre os assuntos 
    abordados no momento da coleta aleatória.

    As outras informações de datas, horários, ids, quantidades de retweets, etc. são fictícios e gerados para que
    os dados fiquem exatamente como ficariam no caso de se seguir o passo a passo descrito acima com dados de qualquer outro usuário.
    '''


# Página de análise
def analysis_page():

    # Upload do arquivo
    st.sidebar.header('**Upload do arquivo**')
    uploaded_file = st.sidebar.file_uploader("", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = preprocess(df)

        # Tipos de análise
        st.sidebar.header('**Análises**')
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

    # Estatísticas básicas
    st.header('**Estatísticas básicas**')
    st.write('Nº total de tweets: ', len(df))
    st.write('Nº total de retweets: ', sum(df.retweet_count))
    st.write('Nº total de curtidas: ', sum(df.favorite_count))
    st.write('Dia do primeiro tweet enviado: ', min(df.date))
    st.write('Dia do último tweet enviado: ', max(df.date))

    # Com mais retweets
    st.header('**O mais retwitado**')
    max_retweet = max(df.retweet_count)
    st.table(df['full_text'][df['retweet_count'] == max_retweet])

    # Com mais curtidas
    st.header('**O mais curtido**')
    max_favorite = max(df.favorite_count)
    st.table(df['full_text'][df['favorite_count'] == max_favorite])

    # Gráfico donnut de retweets
    st.header('**Tweets com retweets**')
    graph_retweet(df)

    # Gráfico donnut de curtidas
    st.header('**Tweets com curtidas**')
    graph_favorite(df)


# Análise temporal (Análise 2)
def analysis_2(df):

    # Escolha do período de análise
    st.header('**Escolha o período de análise**')
    sns.set_style("darkgrid")
    df = slider_period(df)

    # Gráfico com todo o período
    st.header('**Tweets enviados no período**')
    graph_period(df)

    # Gráfico de tweets por mês
    st.header('**Total de tweets por mês**')
    graph_month(df)

    # Gráfico de tweets por dia da semana
    st.header('**Total de tweets por dia da semana**')
    graph_weekday(df)

    # Gráfico de tweets por ano
    st.header('**Total de tweets por ano**')
    graph_year(df)



# Word Cloud (Análise 3)
def analysis_3(df):

    # Remoção de palavras a pedido do usuário
    st.header('**Remoção de palavras**')
    words = stopwords_general(df)
    words = stopwords_user(words)

    # Word Cloud
    st.header('**Nuvem de palavras**')
    try: 
        graph_wordcloud(words)
    except:
        st.info('Não foi possível carregar a Word Cloud')

    # Gráfico de frequência
    st.header('**Palavras mais frequentes**')
    graph_freq(words)



## Função de Pré processamento ## --------------------------------------------------------------------------------------

# Função de Pré processamento
def preprocess(df):

    get_datetime = lambda s: datetime.strptime(s, '%a %b %d %H:%M:%S %z %Y')
    get_weekday = lambda d: calendar.day_name[d.weekday()]
    get_month = lambda d: calendar.month_name[d.month]
    get_hour = lambda d: d.hour
    get_year = lambda d: d.year
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

## Função da Análise Temporal ## --------------------------------------------------------------------------------------

# Slider para a escolha do período
def slider_period(df):

    # Definição do range
    min_date = min(df.date)
    max_date = max(df.date)
    range_date = st.date_input("Insira o período de início e fim que deseja analisar no formato (YYYY/MM/DD - YYYY/MM/DD)", [min_date, max_date])

    # Criar período caso não ocorra erro
    try:
        df_subset = df[(df['date']>= range_date[0]) & (df['date']<= range_date[1])]
        
        if st.button('Resetar período'):
            return df
        else:
            return df_subset
    except:
        st.error('Inisira um período válido no formato YYYY/MM/DD – YYYY/MM/DD')
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


# Gráfico tweets no mês
def graph_month(df):

    # Agrupamento dos dados
    df_month = Counter(df.month)
    print(df_month)
    desired_order_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_month = {k: df_month[k] for k in desired_order_list}

    # Plot do gráfico
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

    # Agrupamento dos dados
    df_weekday = Counter(df.weekday)
    desired_order_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    df_weekday = {k: df_weekday[k] for k in desired_order_list}
    n_weekday = range(len(df_weekday))

    # Plot do gráfico
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

    # Agrupamento dos dados
    df_year = Counter(df.year)
    desired_order_list = sorted(df_year)
    df_year = {k: df_year[k] for k in desired_order_list}

    # Plot do gráfico
    n_year = range(len(df_year))
    plt.figure(figsize = (10,5))
    ax = plt.subplot()
    ax.set_xticks(n_year)
    ax.set_xticklabels(df_year.keys())
    plt.bar(n_year, df_year.values())
    plt.xlabel('Ano')
    plt.ylabel('Quantidade de tweets')
    st.pyplot()

## Funções da Análise Word Cloud ## --------------------------------------------------------------------------------------


# Limpeza dos dados
def stopwords_general(df):

    # Função para substituir acentos por seu equivalente sem acento
    def substituir_acentos(txt, codif='utf-8'):
        return normalize('NFKD', txt).encode('ASCII', 'ignore')

    # Extração do texto
    raw_tweets = []
    for tweets in df['full_text']:
        raw_tweets.append(tweets)

    # Limpeza de caracteres especiais
    raw_string = ''.join(raw_tweets)
    no_links = re.sub(r'http\S+', '', raw_string)
    no_acentos = str(substituir_acentos(no_links))[2:-1]
    no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_acentos) 
    no_mark= re.sub(r'(\s)@\w+', r'\1', no_unicode)
    no_special_characters = re.sub('[^A-Za-z ]+', '', no_mark)

    # Remoção de stopwords - lista com 500
    with open('stopwords-pt.txt', 'r', encoding="utf-8") as file:
        words_list = file.read().replace('\n', ',')
        STOPWORDS = words_list.split(",")

    words = no_special_characters.split(" ")
    words = [w for w in words if len(w) > 2]  # Ignorar artigos a, o, as, os, um...
    words = [w.lower() for w in words]
    words = [w for w in words if w not in STOPWORDS]

    # Remoção de stopwords extras
    with open('stopwords-extra.txt', 'r', encoding="utf-8") as file:
        words_list_extra = file.read().replace('\n', ',')
        STOPWORDS_extra = words_list_extra.split(",")

    words = [w for w in words if w not in STOPWORDS_extra]

    return words


# Stopwords inseridas pelo usuário
def stopwords_user(words):

    # Solicitar palavras
    words_list_user = st.text_input('Insira todas as palavras que deseja remover da Word Cloud (separar as palavras com barras "/")', 'ate/sao/tao')
    STOPWORDS_user = words_list_user.split("/")
    words_new = [w for w in words if w not in STOPWORDS_user]

    # Display bonito das palavras
    options = st.multiselect(
        'Palavras removidas',
        STOPWORDS_user,
        STOPWORDS_user)

    return words_new


# Gráfico Word Cloud
def graph_wordcloud(words):
    from wordcloud import WordCloud
    wordcloud = WordCloud(background_color="white", width = 1000, height = 500, scale=1).generate(' '.join(words))
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot()


# Gráfico com a frequência das palavras
def graph_freq(words):
    df_palavras = FreqDist(words)
    fig = plt.figure(figsize=(10,5))
    df_palavras.plot(20, cumulative=False)
    st.pyplot()

## Funções da Análise Visão Geral ## --------------------------------------------------------------------------------------

# Gráfico donnuts de favoritos
def graph_favorite(df):
    
    # Agrupamento dos dados
    df_favorite = Counter(df.favorite)
    labels = list(df_favorite.keys()) 
    values = list(df_favorite.values())

    # Plot do gráfico
    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))
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


# Gráfico donnuts de retweets
def graph_retweet(df):

    # Agrupamento dos dados
    df_retweet = Counter(df.retweet)
    labels = list(df_retweet.keys()) 
    values = list(df_retweet.values())

    # Plot do gráfico
    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))
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
