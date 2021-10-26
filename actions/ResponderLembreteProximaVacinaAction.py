from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, ReminderScheduled, ReminderCancelled
from os import path
from typing import Any, Text, Dict, List
from datetime import datetime, timedelta


class ActionCadastrarLembrete(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_cadastrar_lembrete_proxima_dose"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dia = f'{tracker.get_slot("dia")}'.zfill(2)
        mes = f'{tracker.get_slot("mes")}'.zfill(2)
        ano = tracker.get_slot("ano")

        QTD_SEGUNDOS_EM_UM_DIA = 86400

        data_final_informada = f'{dia}-{mes}-{ano}'
        data_inicial = ''
        data_final = ''

        try:
            data_inicial = datetime.strptime(
                datetime.today().strftime('%d-%m-%Y'), '%d-%m-%Y')
            data_final = datetime.strptime(data_final_informada, '%d-%m-%Y')
        except:
            mensagem_erro = f'Parece que a data {data_final_informada} não é válida 🥺. Lembre-se de informar uma data futura 😉'
            dispatcher.utter_message(text=mensagem_erro)
            return [AllSlotsReset()]

        diferenca_entre_data_final_e_inicial = (data_final - data_inicial)

        if diferenca_entre_data_final_e_inicial.days <= 0:
            mensagem_erro = f'Parece que a data {data_final_informada} não é válida 🥺. Lembre-se de informar uma data futura 😉'
            dispatcher.utter_message(text=mensagem_erro)
            return [AllSlotsReset()]

        quantidade_dias = abs((data_final - data_inicial).days)

        quantidade_segundos = quantidade_dias * QTD_SEGUNDOS_EM_UM_DIA

        dispatcher.utter_message(
            f"Eu lembrarei você na data de {data_final_informada}")

        date = datetime.now() + timedelta(seconds=quantidade_segundos)
        entities = tracker.latest_message.get("entities")

        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time=date,
            entities=entities,
            name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder, AllSlotsReset()]


class ActionLembrarUsuario(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_enviar_lembrete_da_proxima_dose_da_vacina"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            f"Hoje é o dia de se vacinar 🥳, lembre-se de ir ao posto de saúde para tomar a outra dose da vacina do Covid-19")

        return []
