class InvalidVariable():
    def __init__(self, variable):
        f"""
        Invalid variable {variable} given at line {}
        (Basically, the variable you called doesn't exist, define it before you call it)
        """
        print(f"Invalid Variable {variable} given")