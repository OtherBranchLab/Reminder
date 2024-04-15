from state.state import State


class StateMachine:
    __states: dict[str, State] = {}
    __dates: dict[str, any] = {}

    @classmethod
    def set_state(cls, context: str, state: State, data: any = None):
        if data:
            cls.__dates[context] = data
        cls.__states[context] = state

    @classmethod
    def remove_state(cls, context: str):
        if context in cls.__states:
            del cls.__states[context]
        if context in cls.__dates:
            del cls.__dates[context]

    @classmethod
    def has_state(cls, context: str, state: type):
        if context in cls.__states:
            received_state = cls.__states.get(context)
            if received_state:
                if state == received_state:
                    return True
        return False

    @classmethod
    def get_state(cls, context: str):
        return cls.__states.get(context)

    @classmethod
    def get_data(cls, context: str):
        return cls.__dates.get(context)
