from state_machine import StatesManager


def test_state_manager_init_method():
    """Testing the state manager class init method
    """
    # Setup/Execute
    state_manager = StatesManager()

    # Verify
    assert state_manager.initial_state == None and \
           state_manager.last_state == None and \
           state_manager.current_state == None and \
           state_manager.states == [] 