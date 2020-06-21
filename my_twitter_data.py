import streamlit as st
import webbrowser
import pandas as pd


def main_page():

    st.title('My Twitter Data')

    '''Faça a análise dos dados do seu Twitter de um jeito fácil e rápido!'''

    '''O `My Twitter Data` é um aplicativo criado para que qualquer pessoa com uma conta no twitter
    consiga analisar seus dados de perfil sem a necessidade de instalar programas em seu computador. 
    É tudo online e para começar basta completar alguns passos.
    '''

    '''Confira o vídeo explicativo:'''

    st.video('https://youtu.be/1HhTusjL42k')


def requestdata_page():

    st.title('Obtendo dados do Twitter')

    '''
    Você sabia que pode solicitar um arquivo com todos os seus tweets para o Twitter?
    '''

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


def jsontocsv_page():

    st.title('Convertendo dados json para csv')

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


def upload_page():

    st.title('Upload dos dados')

    '''
    Arraste o arquivo para a caixa abaixo ou selecione o local do arquivo no seu computador! 
    '''

    uploaded_file = st.file_uploader("", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)


def analysis_page():
    st.sidebar.markdown('---')
    st.sidebar.header('**Tipo de análise**')
    analysis = st.sidebar.radio("", ('Visão Geral',
                                     'Análise temporal',
                                     'Nuvem de palavras'))


st.sidebar.header('**Passo a passo**')

page = st.sidebar.radio("", ('Sobre o My Twitter Data',
                             'Obtendo dados do Twitter',
                             'Convertendo dados json para csv',
                             'Upload dos dados',
                             'Análise dos dados'))

if page == 'Sobre o My Twitter Data':
    main_page()
if page == 'Obtendo dados do Twitter':
    requestdata_page()
if page == 'Convertendo dados json para csv':
    jsontocsv_page()
if page == 'Upload dos dados':
    upload_page()
if page == 'Análise dos dados':
    analysis_page()
