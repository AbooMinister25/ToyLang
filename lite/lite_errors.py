# class InvalidVariable():
#     def __init__(self, variable, line_number, column):
#         f"""
#         Invalid variable {variable} given at line {}
#         (Basically, the variable you called doesn't exist, define it before you call it)
#         """
#         print(f"Invalid Variable {variable} given")

class MissingToken():
    def __init__(self, token, line_number, column):
        error = f'''
        Missing {token} at line number {line_number} on column {column}
        (Basically, you forgot to add a token to your statement, this is pretty common, its usually a forgotton semicolon, be sure to check if its there)
        '''
        print(error)