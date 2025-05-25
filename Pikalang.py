print(r"""
   ▄███████▄  ▄█     ▄█   ▄█▄    ▄████████  ▄█          ▄████████ ███▄▄▄▄      ▄██████▄  
  ███    ███ ███    ███ ▄███▀   ███    ███ ███         ███    ███ ███▀▀▀██▄   ███    ███ 
  ███    ███ ███▌   ███▐██▀     ███    ███ ███         ███    ███ ███   ███   ███    █▀  
  ███    ███ ███▌  ▄█████▀      ███    ███ ███         ███    ███ ███   ███  ▄███        
▀█████████▀  ███▌ ▀▀█████▄    ▀███████████ ███       ▀███████████ ███   ███ ▀▀███ ████▄  
  ███        ███    ███▐██▄     ███    ███ ███         ███    ███ ███   ███   ███    ███ 
  ███        ███    ███ ▀███▄   ███    ███ ███▌    ▄   ███    ███ ███   ███   ███    ███ 
 ▄████▀      █▀     ███   ▀█▀   ███    █▀  █████▄▄██   ███    █▀   ▀█   █▀    ████████▀  
                    ▀                      ▀                                             
""")

def print_guide():
    print(r'''
🔹 PIKALang - Quick Start Guide 🔹

→ let x = 5
    Define a variable.

→ print x
    Print a variable's value.

→ print "Hello" OR print 'Hello'
    Print a string literal.

→ if x > 3 then { print "ok" } else { print "not ok" }
    Basic if-else condition.

→ while x > 0 then { print x; let x = x - 1 }
    Loop with a condition.

→ exit / quit
    To exit the interpreter.

Supported operators: >, <, ==, !=, >=, <=
Wrap multiple commands inside { } and separate them with ;

Enjoy coding in PIKALang!
''')

print_guide()

variables = {}


def condition_check(condition):
            if ">=" in condition:
                left, right = condition.split(">=", 1)
                left = left.strip()
                right = right.strip()
                value1 = eval(left, {}, variables)
                value2 = eval(right, {}, variables)
            
                if value1 >= value2:
                    # parse_and_execute(statement)
                    return 1

            elif "<=" in condition:
                left, right = condition.split("<=", 1)
                left = left.strip()
                right = right.strip()
                value1 = eval(left, {}, variables)
                value2 = eval(right, {}, variables)
            
                if value1 <= value2:
                    # parse_and_execute(statement)
                    return 1
            elif "==" in condition:
                left, right = condition.split("==", 1)
                left = left.strip()
                right = right.strip()
                value1 = eval(left, {}, variables)
                value2 = eval(right, {}, variables)
            
                if value1 == value2:
                    # parse_and_execute(statement)
                    return 1
                    
            elif "!=" in condition:
                left, right = condition.split("!=", 1)
                left = left.strip()
                right = right.strip()
                value1 = eval(left, {}, variables)
                value2 = eval(right, {}, variables)
            
                if value1 != value2:
                    # parse_and_execute(statement)
                    return 1

            elif "<" in condition:
                left, right = condition.split("<", 1)
                left = left.strip()
                right = right.strip()
                value1 = eval(left, {}, variables)
                value2 = eval(right, {}, variables)
            
                if value1 < value2:
                    # parse_and_execute(statement)
                    return 1
            elif ">" in condition:
                left, right = condition.split(">", 1)
                left = left.strip()
                right = right.strip()
                value1 = eval(left, {}, variables)
                value2 = eval(right, {}, variables)
            
                if value1 > value2:
                    # parse_and_execute(statement)
                    return 1
                
            return False



def executing_statement(statement):
    if statement.startswith("{") and statement.endswith("}"):
                    block = statement[1:-1]
                    filtered_statement = block.split(";")

                    for stmt in filtered_statement:
                        stmt = stmt.strip()
                        if stmt:
                            parse_and_execute(stmt)
    else:
         parse_and_execute(statement)


def parse_and_execute(code):
    if code.startswith("let "):
        try:
            _, rest = code.split("let ", 1)
            var, expr = rest.split("=", 1)
            var = var.strip()
            expr = expr.strip()

            value = eval(expr, {}, variables)
            variables[var] = value
        except Exception as e:
            print(f"Error: {e}")


    if code.startswith("print "):
        try:
            _, print_statement = code.split("print ", 1)
            print_statement = print_statement.strip()

            if (print_statement.startswith('"') and print_statement.endswith('"')) or \
   (print_statement.startswith("'") and print_statement.endswith("'")):
                 block = print_statement[1:-1]
                 print(block)
            else:
                value = eval(print_statement, {}, variables)
                print(value)
        except Exception as e:
            print(f"Error: {e}")


    if code.startswith("if "):
        try:
            _, rest = code.split("if ", 1)
            condition, statement = rest.split("then",1)
            condition = condition.strip()
            statement = statement.strip()
            if "else" in statement:
                if_statement,else_statement = statement.split("else",1)
                if_statement = if_statement.strip()
                else_statement = else_statement.strip()

                if(condition_check(condition)):
                    executing_statement(if_statement)
                    # parse_and_execute(if_statement)
                else:
                    executing_statement(else_statement)
                    # parse_and_execute(else_statement)
            else:
                if(condition_check(condition)):
                    executing_statement(statement)
                
        except Exception as e:
            print(f"Error: {e}")


    if code.startswith("while "):
        try:
            _, rest = code.split("while ", 1)
            condition, statement = rest.split("then",1)
            condition = condition.strip()
            statement = statement.strip()

            while condition_check(condition):
                parse_and_execute(statement)
        except Exception as e:
            print(f"Error: {e}")



print("PIKALang Interpreter. Fire away your commands.")
while True:
    try:
        code = input(">>> ").strip()

        if code.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        parse_and_execute(code)

    except KeyboardInterrupt:
        print("\nExiting.")
        break
