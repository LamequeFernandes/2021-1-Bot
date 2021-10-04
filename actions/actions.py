# -*- coding: utf-8 -*-

import os
import time
import shutil
import requests
import requests
import patoolib
import pandas as pd

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from os import path
from typing import Any, Text, Dict, List

diretorio = path.join(path.dirname(path.realpath(__file__)), 'covid_data')

class DownloadDados(Action): 

    def __init__(self):
        self.url = 'https://data.brasil.io/dataset/covid19/caso.csv.gz'
        self.arquivo = 'dados_covid_csv.gz'
        self.caminho_arquivo = path.join(diretorio, self.arquivo)
        self.TEMPO_LIMITE_PARA_ATUALIZACAO_EM_DIAS = 1

    def name(self) -> Text:
        return 'action_download_dados'

    def arquivo_csv_existe(self) -> bool:
        return path.isfile(self.caminho_arquivo)

    def arquivo_csv_baixado_ha_mais_de_um_dia(self) -> bool:
        SEGUNDOS_PARA_DIAS = 60 * 60 * 24
        instante_atual = time.time()
        instante_da_ultima_modificacao_arquivo = os.stat(self.caminho_arquivo).st_mtime

        print(instante_da_ultima_modificacao_arquivo)

        diferenca_de_instante_em_seg = instante_atual - instante_da_ultima_modificacao_arquivo
        print('Diferenca de tempo em segundos', diferenca_de_instante_em_seg)
        print('Diferenca de dias em segundos', diferenca_de_instante_em_seg / SEGUNDOS_PARA_DIAS)

        return (diferenca_de_instante_em_seg / SEGUNDOS_PARA_DIAS) > self.TEMPO_LIMITE_PARA_ATUALIZACAO_EM_DIAS

    def baixar_e_extrair_arquivo_csv(self) -> None:
        print('baixando arquivo atualizado')
        os.remove(path.join(diretorio, 'caso.csv'))
        self.resposta = requests.get(self.url)

        if self.resposta.status_code == requests.codes.OK:
            with open(self.caminho_arquivo, 'wb') as novo_arquivo:
                novo_arquivo.write(self.resposta.content)
                print(f'Download finalizado. Arquivo salvo em: {self.caminho_arquivo}')
        else:
            self.resposta.raise_for_status()

        patoolib.extract_archive(self.caminho_arquivo, outdir=diretorio)
        return

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        arquivo_csv_existe = self.arquivo_csv_existe()
        if not arquivo_csv_existe or (arquivo_csv_existe and self.arquivo_csv_baixado_ha_mais_de_um_dia()):
            self.baixar_e_extrair_arquivo_csv()
        
        return []


class DadosDoCovidPeloCsvAction(Action):

    def name(self) -> Text:
        return 'action_dados_covid_baseados_em_localizacao'
    
    def arquivo_baixado_ha_mais_de_um_dia(self, caminho_do_arquivo: str):
        SEGUNDOS_PARA_DIAS = 60 * 60 * 24
        instante_atual = time.time()
        instante_da_ultima_modificacao_arquivo = os.stat(caminho_do_arquivo).st_mtime

        diferenca_de_instante_em_seg = instante_atual - instante_da_ultima_modificacao_arquivo
        
        return (diferenca_de_instante_em_seg / SEGUNDOS_PARA_DIAS) > self.TEMPO_LIMITE_PARA_ATUALIZACAO

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        uf = tracker.get_slot('uf').upper()
        cidade = tracker.get_slot('cidade').capitalize()

        self.dados = pd.read_csv(
            path.join(diretorio, 'caso.csv'),
            sep = ',',
            decimal = '.'
        )

        dataframe = pd.DataFrame(self.dados)

        pesquisa_por_uf = dataframe.loc[dataframe['state'] == uf]
        if pesquisa_por_uf.empty:
            dispatcher.utter_message(text='Não achei sua UF. Certifique-se que você está digitando corretamente.')
            return [AllSlotsReset()]

        pesquisa_por_ultimo_dado = pesquisa_por_uf.loc[dataframe['is_last'] == True]

        pesquisa_por_cidade = pesquisa_por_ultimo_dado.loc[dataframe['city'] == cidade]
        if pesquisa_por_cidade.empty:
            dispatcher.utter_message(text='Olha, não consegui encontrar a sua cidade. Certifique-se que você está digitando corretamente, incluindo acentos, nome próprio')
            return [AllSlotsReset()]

        pesquisa_por_cidade = pesquisa_por_cidade[
            [
                'date',
                'state', 
                'city', 
                'estimated_population_2019',
                'confirmed',
                'deaths',
                'confirmed_per_100k_inhabitants',
            ]
        ]

        ingles_para_portugues = {
            'date': 'Data',
            'state': 'Estado', 
            'city': 'Cidade', 
            'estimated_population_2019': 'População estimada em 2019',
            'confirmed': 'Confirmados',
            'deaths': 'Mortes',
            'confirmed_per_100k_inhabitants': 'Confirmados a cada 100 mil habitantes',
        }

        mensagem = ''
        
        for rotulo_ingles, content in pesquisa_por_cidade.items():
            rotulo_portugues = ingles_para_portugues[rotulo_ingles]
            mensagem += f'{rotulo_portugues}: {str(content.to_list()[0])}\n'

        dispatcher.utter_message(text=mensagem)
        
        return [AllSlotsReset()]
