from state_machine import State


def fun_entry():
    pass

def fun_exit():
    pass

def fun_routine():
    pass

def fun_decision():
    pass 


def test_state_init_method():
    """Testing the State class init method.
    """
    # Setup
    

    # Execute
    state = State(routine_function= fun_routine, 
                  decision_function=fun_decision,
                  entry_function=fun_entry,
                  exit_function=fun_exit,
                  is_async=False)

    # Verify
    assert state.routine_function.__name__ == fun_routine.__name__ and \
           state.decision_function.__name__ == fun_decision.__name__ and \
           state.entry_function.__name__ == fun_entry.__name__ and \
           state.exit_function.__name__ == fun_exit.__name__ and \
           state.is_async == False and \
           state.next_states == None
    
