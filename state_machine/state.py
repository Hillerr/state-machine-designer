import asyncio 


class State:
    """This class represents the states that makes up the state machine.

    Attributes:
        name (str): The state name
        entry_function (function): A function that will be executed when the state machine's state
            entry on this specific state
        routine_function (function): A function that will be executed on each interaction of the state machine
            when it stay on this specific state.
        exit_function (function): A function that will be executed when the state machine's are leaving
            this this specific state
        decision_function (function): A function that decides, according to the object circunstancies, what state
            will be the next
        is_async (bool): This flag indicates if these object functions should be performed as asynchronous (True) 
            or not (False)
        next_states (`list`): A list of `States` that could be the next. 
    """

    def __init__(self, name, decision_function, routine_function=None, entry_function=None, exit_function=None, is_async=True, next_states=None):
        """State class initialization function.

        Args:
            name (str): The state name
            decision_function (function): A function that decides, according to the object circunstancies, what state
                will be the next
            routine_function (function, optional): A function that will be executed on each interaction of the state machine
                when it stay on this specific state. Defaults to None.
            entry_function (function, optional): A function that will be executed when the state machine's state
                entry on this specific state. Defaults to None.
            exit_function (function, optional): A function that will be executed when the state machine's are leaving
                this this specific state. Defaults to None.
            is_async (bool, optional): This flag indicates if these object functions should be performed as asynchronous (True) 
                or not (False). Defaults to True.
            next_states (`list`, optional): A list of `States` that could be the next, if it's None, the next states will 
                not be verified when there's a state transition. Defaults to None.
        """
        self.name = name
        self.routine_function = routine_function
        self.decision_function = decision_function
        self.entry_function = entry_function
        self.exit_function = exit_function
        self.is_async = is_async
        self.next_states = next_states


    def __eq__(self, other):
        """Verify if this object in equals to other

        Args:
            other (``State``): A ``State`` object

        Returns:
            `bool`: True if both names match, False otherwise
        """
        return self.name == other.name


    def __repr__(self):
        """State class representation method

        Returns:
            `str`: A string representation of the object
        """
        return f"State(name={self.name}, decision_function={self.decision_function.__name__}, routine_function={self.routine_function.__name__}, entry_function={self.entry_function.__name__}, exit_function={self.exit_function.__name__}, is_async={self.is_async}, next_states={[state.name for state in self.next_states if self.next_states is not None]})"
    

    @property
    def name(self):
        """str: The state name"""
        return self._name


    @name.setter
    def name(self, var):
        if not isinstance(var, str):
            raise ValueError(f"Param 'name' must be a string. You passed {var.__class__.__name__}")
        self._name = var

    @property
    def decision_function(self):
        """function: A function that decides, according to the object circunstancies, what state will be the next
        """
        return self._decision_function


    @decision_function.setter
    def decision_function(self, var):
        self._parse_function_attr(var, "decision_function")
        self._decision_function = var


    @property
    def routine_function(self):
        """function: A function that will be executed on each interaction of the state machine when it stay on this specific state."""
        return self._routine_function

    
    @routine_function.setter
    def routine_function(self, var):
        self._parse_function_attr(var, "routine_function")
        self._routine_function = var 


    @property
    def entry_function(self):
        """function: A function that will be executed when the state machine's are leaving
        this this specific state
        """
        return self._entry_function


    @entry_function.setter
    def entry_function(self, var):
        self._parse_function_attr(var, "entry_function")
        self._entry_function = var


    @property
    def exit_function(self):
        """function: A function that will be executed when the state machine's are leaving
        this this specific state
        """
        return self._exit_function


    @exit_function.setter
    def exit_function(self, var):
        self._parse_function_attr(var, "exit_function")
        self._exit_function = var


    @property
    def is_async(self):
        """bool: This flag indicates if these object functions should be performed as asynchronous (True) 
        or not (False)
        """
        return self._is_async


    @is_async.setter
    def is_async(self, var):
        if not isinstance(var, bool):
            raise ValueError(f"Param 'is_async' must be a boolean value. You passed {var}.")
        self._is_async = var 


    @property
    def next_states(self):
        """`list`: A list of `States` that could be the next, if it's None, the next states will 
            not be verified when there's a state transition
        """
        return self._next_states


    @next_states.setter
    def next_states(self, var):
        if var is None:
            self._next_states = var 

        else:
            if not isinstance(var, list):
                raise ValueError(f"Param 'next_states' must be a list of States or None.")
            else:
                for state in var:
                    if not isinstance(state, State):
                        raise ValueError(f"Param 'next_states' must be a list of State. {state.__class__.__name__} is not supported.")
            self._next_states = var


    def _parse_function_attr(self, var, attr):
        """Validates if the var is a callable object.

        Args:
            var (function): callable object
            attr (str): attribute name

        Raises:
            ValueError: If arg 'var' is not callable
        """
        if not callable(var) and var != None:
            raise ValueError(f"Param '{attr}' must be a callable object.")


    def is_next_state(self, state):
        """Verify if state is in the next_states attribute list

        Args:
            state (``State``): A ``State`` object

        Raises:
            ValueError: If state is not a ``State`` object

        Returns:
            bool: True if this State does not contains next states or state in the list, False otherwise
        """
        if not isinstance(state, State):
            raise ValueError(f"Arg 'state' must be a State object.")

        if self.next_states is None:
            return True

        return state in self.next_states

        