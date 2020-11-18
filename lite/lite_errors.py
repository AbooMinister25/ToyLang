class MissingToken():
    def __init__(self, token, line_number, column, context):
        error = f'''
MissingTokenError:
    Missing {token} at line number {line_number} on column {column}:
        {context}
    (Basically, you forgot to add a token to your statement, this is pretty common, its usually a forgotton semicolon, be sure to check if its there)
        '''
        print(error)


class InvalidName():
    def __init__(self, name):
        error = f'''
InvalidNameError:
    Invalid name {name} given.
    (Basically, you supplied an invalid name in your code, probably a variable that doesn't exist, check your code)
        '''
        print(error)


class InvalidType():
    def __init__(self, type):
        error = f'''
InvalidTypeError:
    Invalid type {type} given.
    
    (Basically, you gave an invalid type in your code, maybe a number where there was supposed to be a string, or vice versa)
'''
        print(error)

class InvalidIndex():
    def __init__(self, index):
        error = f'''
InvalidIndexError:
    Index {index} out of range. Invalid index given.
    
    (Basically, you supplied an invalid index, one that doesn't exist, try changing the index your calling)
    
'''
        print(error)

class InvalidSyntax():
    def __init__(self, data=None, column=None, line_number=None, context=None):
        if column != None and line_number != None:
            error = f'''
InvalidSyntaxError:
    Invalid syntax {data} given at line {line_number} column {column}
        {context}
    (Basically, your code is invalid, and is raising this error, try debugging it, and finding whats wrong)
'''
        else:
            error = f'''
InvalidSyntaxError:
    Invalid syntax given.
    
    (Basically, your code is invalid, and is raising this error, try debugging it, and finding whats wrong)
'''