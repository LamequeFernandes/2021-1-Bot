import pytest
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from actions.ResponderQuantidadeVacinadosPorPeriodoAction import ResponderQuantidadeVacinadosPorPeriodoAction


class FakeDomain:
    def __init__(self):
        pass


class FakeTracker:
    def get_slot(self, slot):
        pass


class ResponderQuantidadeVacinadosPorPeriodoActionTest:

    def setup(self, mocker):
        self.service = ResponderQuantidadeVacinadosPorPeriodoAction()
        self.dispatcher = CollectingDispatcher()
        self.tracker = FakeTracker()
        self.domain = FakeDomain()

    def test_name(self, mocker):
        self.setup(mocker)
        assert self.service.name() == 'action_responder_quantidade_vacinados_por_periodo'

    def test_bot(self, mocker):
        self.setup(mocker)
        mocker.patch.object(self.tracker, "get_slot",
                            return_value="23/12/1970")

        self.service.run(self.dispatcher, self.tracker, self.domain)
        assert self.dispatcher.messages[0]['text'].startswith(
            'Não consegui encontrar nenhum registro para a data 23/12/1970-23/12/1970-23/12/1970 🥺. Lembre-se de informar valores válidos e somente o número do dia, do mês e do ano 😉')


def test_ResponderQuantidadeVacinadosPorPeriodoAction(mocker):
    ResponderQuantidadeVacinadosPorPeriodoActionTest().test_bot(mocker)
    ResponderQuantidadeVacinadosPorPeriodoActionTest().test_name(mocker)
