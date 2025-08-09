from abc import ABC, abstractmethod

class AbstractTelegramBot(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def send_question(self):
        pass

    @abstractmethod
    def handle_answer(self):
        pass