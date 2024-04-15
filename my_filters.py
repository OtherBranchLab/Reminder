from aiogram.filters import Filter
from aiogram.types import Message

from state.state_machine import StateMachine


class IsState(Filter):
    def __init__(self, state_type: type) -> None:
        self.state_type = state_type

    async def __call__(self, message: Message) -> bool:
        return StateMachine.has_state(str(message.chat.id), self.state_type)
