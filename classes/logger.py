import time
class Logger:
    '''Log system anf jeneral cheks'''
    def log_action(action_type:str, details:str)->None:
        print(f'action type: {action_type}, detalis: {details} at {time.ctime()}')

