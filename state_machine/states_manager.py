import asyncio
from .state import State
from .exceptions import *


class StatesManager:
    """States Manager class

    This class will be responsible for executing the States functions and updating
    the state machine current state. Also verify the integrity of the machine.

    Attributes:
        initial_state (``State``): The first ``State`` that the state machine will
            execute
        current_state (``State``): The current ``State`` that the state machine is
            performing
        last_state (``State``): The last ``State`` that the state machine had
            performed
        states (`list` of ``States``): All the ``States`` that make up the state machine
    """

    def __init__(self):
        """StatesManager initialization method.
        """
        self.initial_state = None
        self.last_state = None
        self.current_state = None
        self._states = [] 


    @property
    def initial_state(self):
        """``State``: The first ``State`` that the state machine will execute"""
        return self._initial_state

    
    @initial_state.setter
    def initial_state(self, var):
        if var is None:
            self._initial_state = var
            return

        if var is not None and not isinstance(var, State):
            raise ValueError(f"Param 'initial_state' must be a State object. You passed {var.__class__.__name__}.")

        if not self._exist_state(var):
            raise InitialStateError(f"There is no State with name {var.name} added yet. Valid states are: {state.name for state in self.states if self.states is not None}")

        self._initial_state = var 


    @property
    def last_state(self):
        """``State``: The last ``State`` that the state machine had performed"""
        return self._last_state


    def last_state(self):
        if var is None:
            self._last_state = var
            return

        if var is not None and not isinstance(var, State):
            raise ValueError(f"Param 'last_state' must be a State object. You passed {var.__class__.__name__}.")

        if not self._exist_state(var):
            raise LastStateError(f"There is no State with name {var.name} added yet. Valid states are: {state.name for state in self.states if self.states is not None}")

        self._initial_state = var 


    @property
    def current_state(self):
        """``State``: The current ``State`` that the state machine is performing
        """
        return self._current_state


    @current_state.setter
    def current_state(self, var):
        if var is None:
            self._current_state = var
            return

        if var is not None and not isinstance(var, State):
            raise ValueError(f"Param 'current_state' must be a State object. You passed {var.__class__.__name__}.")

        if not self._exist_state(var):
            raise CurrentStateError(f"There is no State with name {var.name} added yet. Valid states are: {state.name for state in self.states if self.states is not None}")

        self._current_state = var 


    @property
    def states(self):
        """`list` of ``States``: All the ``States`` that make up the state machine"""
        return self._states


    def _exist_state(self, state):
        """Verify if there is any other state with 
        the same name.

        Args:
            state (``State``): A ``State`` object
        """
        return state in self.states


    def add_state(self, *args):
        """Add a state to the States Manager

        Args:
            args (``State``): The state that will be added

        Raises:
            ValueError: If 'state' is not a ``State`` object
            AddStateError: If already exists a state with the same name
        """
        for arg in args:
            if not isinstance(arg, State):
                raise ValueError(f"Param 'state' must be a State object. You passed {arg.__class__.__name__}.")

            if self._exist_state(arg):
                raise AddStateError(f"Cannot add an already existing state")

            self.states.append(arg)


    def get_state(self, state_name):
        """Get a state by its name

        Args:
            state_name (str): The name of the state to be returned

        Raises:
            ValueError: If state_name is not a string

        Returns:
            ``State``: The requested state, if there's no state with this name, returns None
        """
        if not isinstance(state_name, str):
            raise ValueError(f"Param 'state_name' must be a str. You passed a {state_name.__class__.__name__} object.")

        state = [state for state in self.states if state.name == state_name]

        if len(state) == 0:
            return None
        else:
            return state[0]

