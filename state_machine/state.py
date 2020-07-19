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

    def __init__(self, decision_function, routine_function=None, entry_function=None, exit_function=None, is_async=True, next_states=None):
        """State class initialization function.

        Args:
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
        self.routine_function = routine_function
        self.decision_function = decision_function
        self.entry_function = entry_function
        self.exit_function = exit_function
        self.is_async = is_async
        self.next_states = next_states


        @property
        def decision_function(self):
            """function: A function that decides, according to the object circunstancies, what state will be the next
            """
            return self._decision_function


        @decision_function.setter
        def decision_function(self, var):
            self._parse_function_attr(var, "decision_function")
            self.decision_function = var


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
                        if not isinstance(var, State):
                            raise ValueError(f"Param 'next_states' must be a list of State. {type(state)} is not supported.")
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