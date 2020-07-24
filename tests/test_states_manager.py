from state_machine import StatesManager, State
from state_machine.exceptions import *
import pytest

def fun_entry():
    pass

def fun_exit():
    pass

def fun_routine():
    pass

def fun_decision():
    pass 


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


def test_states_manager_add_state_method():
    """Testing the StatesManager add_state method
    """
    # Setup

    state1 = State(
        name="state1",
        routine_function= fun_routine, 
        decision_function=fun_decision,
        entry_function=fun_entry,
        exit_function=fun_exit,
        is_async=False
    )

    state2 = State(
        name="state2",
        routine_function= fun_routine, 
        decision_function=fun_decision,
        entry_function=fun_entry,
        exit_function=fun_exit,
        is_async=False
    )

    state3 = State(
        name="state3",
        routine_function= fun_routine, 
        decision_function=fun_decision,
        entry_function=fun_entry,
        exit_function=fun_exit,
        next_states=[state1],
        is_async=False
    )

    state_manager = StatesManager()

    # Execute
    state_manager.add_state(state1, state2, state3)

    # Verify
    assert len(state_manager.states) == 3


def test_states_manager_add_state_method_wrong():
    """Testing the StatesManager add_state method with duplicated states
    """
    # Setup

    state1 = State(
        name="state1",
        routine_function= fun_routine, 
        decision_function=fun_decision,
        entry_function=fun_entry,
        exit_function=fun_exit,
        is_async=False
    )

    state2 = State(
        name="state2",
        routine_function= fun_routine, 
        decision_function=fun_decision,
        entry_function=fun_entry,
        exit_function=fun_exit,
        is_async=False
    )

    state_manager = StatesManager()

    # Execute / Verify
    with pytest.raises(AddStateError):
        assert state_manager.add_state(state1, state2, state2)


def test_states_manager_get_state_method():
    """Testing the StatesManager get_state method
    """
    # Setup

    state1 = State(
        name="state1",
        routine_function= fun_routine, 
        decision_function=fun_decision,
        entry_function=fun_entry,
        exit_function=fun_exit,
        is_async=False
    )

    state2 = State(
        name="state2",
        routine_function= fun_routine, 
        decision_function=fun_decision,
        entry_function=fun_entry,
        exit_function=fun_exit,
        is_async=False
    )

    state3 = State(
        name="state3",
        routine_function= fun_routine, 
        decision_function=fun_decision,
        entry_function=fun_entry,
        exit_function=fun_exit,
        next_states=[state1],
        is_async=False
    )

    state_manager = StatesManager()

    state_manager.add_state(state1, state2, state3)

    # Execute
    received_state1 = state_manager.get_state('state1')
    received_state2 = state_manager.get_state('state2')
    received_state3 = state_manager.get_state('state3')

    # Verify
    assert received_state1 == state1 and \
           received_state2 == state2 and \
           received_state3 == state3


def test_states_manager_get_state_method_non_existing_state():
    """Testing the get_state method with non existing state
    """
    # Setup
    state1 = State(
        name="state1",
        routine_function= fun_routine, 
        decision_function=fun_decision,
        entry_function=fun_entry,
        exit_function=fun_exit,
        is_async=False
    )

    state_manager = StatesManager()

    state_manager.add_state(state1)

    # Execute
    received_state = state_manager.get_state('state2')

    assert received_state == None