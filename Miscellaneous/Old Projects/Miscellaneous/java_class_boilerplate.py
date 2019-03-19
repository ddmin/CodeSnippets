TAB = '    '
FILE_PATH  = input("File location: ")

class_ = input("Class Name: ")
instance_variables = []

variable = None
while variable != '':
    variable = input("Variable name: ")
    variable_type = input("Variable type: ")
    instance_variables.append((variable, variable_type))
instance_variables = instance_variables[:-1]

java_code = 'public class {}'.format(class_.capitalize()) + ' {\n'

for var, typ in instance_variables:
    java_code += TAB + f'private {typ} {var};\n'
java_code += TAB + 'public {}'.format(class_.capitalize()) + '() {\n'

for var, typ in instance_variables:
    java_code += TAB + TAB + f'{var} = '
    if typ == 'int' or typ == 'double':
        java_code += '0;'
    elif typ == 'boolean':
        java_code += 'false;'
    else:
        java_code += '  ;'
    java_code += '\n'

java_code += TAB + '}\n'

java_code += TAB + 'public {}'.format(class_.capitalize())
java_code += '(' 
instance_field = ''
for var, typ in instance_variables:
    instance_field += f'{typ} {var}, '
java_code += instance_field[:-2] + ') {\n'

for var, typ in instance_variables:
    java_code += TAB + TAB + f'this.{var} = {var};\n'

java_code += TAB + '}\n'

for var, typ in instance_variables:
    java_code += TAB + f'public {typ} get{var.capitalize()}()' + ' {\n'
    java_code += TAB + TAB + f'return this.{var};\n'
    java_code += TAB + '}\n'

for var, typ in instance_variables:
    java_code += TAB + f'public void set{var.capitalize()}({typ} {var})' + '{\n'
    java_code += TAB + TAB + f'this.{var} = {var};\n'
    java_code += TAB + '}\n'

java_code += '}'

with open(FILE_PATH + '\\' + class_ + '.java', 'w') as f:
    f.write(java_code)