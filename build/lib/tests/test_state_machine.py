from state_machine import StateMachine, State
import pytest

def fun_entry():
    pass

def fun_exit():
    pass

def fun_routine():
    pass

def fun_decision():
    pass 



def test_state_machine_init_method():
    """Basic testing for the State Machine init method
    """
    # Setup
    state_machine = StateMachine()

    # Setup
    def decision():
        return 'state2'

    def decision2():
        return 'state3'

    state1 = State(
        name="state1",
        routine_function= fun_routine, 
        decision_function=decision,
        entry_function=fun_entry,
        exit_function=fun_exit,
        is_async=False
    )

    state2 = State(
        name="state2",
        routine_function= fun_routine, 
        decision_function=decision2,
        entry_function=fun_entry,
        exit_function=fun_exit,
        is_async=False
    )

    state3 = State(
        name="state3",
        routine_function= fun_routine, 
        decision_function=decision,
        is_async=False
    )

    state_machine.add_states(state3, state2, state1)
    state_machine.initial_state = "state1"


def test_state_machine_complete():
    """Testing the complete state_machine application
    """
    class MyClass:
        def __init__(self):
            self.state1_entry_variable = False
            self.state1_exit_variable = False
            self.state1_routine_variable = False

            self.state2_entry_variable = False
            self.state2_exit_variable = False
            self.state2_routine_variable = False

            self.state3_entry_variable = False
            self.state3_exit_variable = False
            self.state3_routine_variable = False

        def func_exit_state1(self):
            self.state1_exit_variable = True

        def func_entry_state1(self):
            self.state1_entry_variable = True

        def func_routine_state1(self):
            self.state1_routine_variable = True

        def func_decision_state1(self):
            return 'state2'


        def func_exit_state2(self):
            self.state2_exit_variable = True

        def func_entry_state2(self):
            self.state2_entry_variable = True

        def func_routine_state2(self):
            self.state2_routine_variable = True

        def func_decision_state2(self):
            return 'state3'


        def func_exit_state3(self):
            self.state3_exit_variable = True

        def func_entry_state3(self):
            self.state3_entry_variable = True

        def func_routine_state3(self):
            self.state3_routine_variable = True

        def func_decision_state3(self):
            return 'state1'

    my_class = MyClass()

    state1 = State(
        name="state1",
        routine_function=my_class.func_routine_state1, 
        decision_function=my_class.func_decision_state1,
        entry_function=my_class.func_entry_state1,
        exit_function=my_class.func_exit_state1,
        is_async=False
    )

    state2 = State(
        name="state2",
        routine_function=my_class.func_routine_state2, 
        decision_function=my_class.func_decision_state2,
        entry_function=my_class.func_entry_state2,
        exit_function=my_class.func_exit_state2,
        is_async=False
    )

    state3 = State(
        name="state3",
        routine_function=my_class.func_routine_state3, 
        decision_function=my_class.func_decision_state3,
        entry_function=my_class.func_entry_state3,
        exit_function=my_class.func_exit_state3,
        is_async=False
    )

    state_machine = StateMachine()

    state_machine.add_states(state1, state2, state3)
    state_machine.initial_state = 'state1'

    # Execute
    for i in range(3):
        state_machine.run()

    # Verify if all my_class attribute are true
    for key in my_class.__dict__:
        # Verify if all attributes were setted
        if getattr(my_class, key) != True:
            assert True

    assert True


