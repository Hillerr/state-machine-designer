import asyncio
from .states_manager import StatesManager
from .state import State
from .exceptions import *


class StateMachine:
    """State Machine class

    This class is responsible for adding the states and executing them.

    Attributes:
        initial_state (str): initial state name 
        current_state (str): current state name
        last_state (str): last state name
        _states_manager (``StatesManager``): The object to manager and parse all the states and transactions
    """

    def __init__(self):
        """State Machine initialization method
        """
        self._state_manager = StatesManager()


    @property
    def initial_state(self):
        """str: initial state name 
        """
        return self._state_manager.initial_state.name 


    @initial_state.setter
    def initial_state(self, var):
        self._state_manager.initial_state = self._state_manager.get_state(var)


    @property
    def current_state(self):
        """str: current state name
        """
        return self._state_manager.current_state.name 


    @property
    def last_state(self):
        """str: last state name
        """
        return self._state_manager.last_state.name 


    def add_states(self, *args):
        """Add multiple states to the state machine

        Args:
            args (``State``): State objects that will be added.
        """
        self._state_manager.add_state(*args)


    def create_state(self, state_name, decision_function, routine_function=None, entry_function=None, exit_function=None):
        """Create a state and add to the state machine

        Args:
            state_name (str): The state name
            decision_function (function): A function that decides, according to the object circunstancies, what state
                will be the next
            routine_function (function, optional): A function that will be executed on each interaction of the state machine
                when it stay on this specific state. Defaults to None.
            entry_function (function, optional): A function that will be executed when the state machine's state
                entry on this specific state. Defaults to None.
            exit_function (function, optional): A function that will be executed when the state machine's are leaving
                this this specific state. Defaults to None.
        """
        self.add_states(State(
            state_name, 
            decision_function, 
            routine_function,
            entry_function,
            exit_function
        ))


    def run(self):
        """Execute the state machine
        """
        if self._state_manager.initial_state is None:
            raise InitialStateError(f"Before running the state machine you must define a initial state. You can set it by self.initial_state = 'state_name'")

        self._state_manager.execute_current_state_functions()