ops_order = [['(', ')'], ['*', '/'], ['+', '-']]
b_serial_no = 0
variables = {}


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def attach(self, left, right):
        self.left = left
        self.right = right


def build_tree(var: str, start: int, end: int):
    global b_serial_no
    ops, brackets = [[], []], []
    brackets_stack = []
    in_bracket = False
    operands = {}
    last_node = None

    for i in range(start, end):
        if eq[i] == '(':
            brackets_stack.append(i)
            in_bracket = True
        elif eq[i] == ')':
            b_start = brackets_stack.pop()
            if len(brackets_stack) == 0:
                in_bracket = False
                b_serial_no += 1
                var_name = str(b_serial_no)
                operands[b_start] = (b_start, i, var_name)
                operands[i] = (b_start, i, var_name)
                brackets.append((b_start + 1, i - 1, var_name))
        elif in_bracket:
            continue
        elif eq[i] in ops_order[1]:
            ops[0].append(i)
        elif eq[i] in ops_order[2]:
            ops[1].append(i)
        else:
            variables[eq[i]] = Node(eq[i])
            operands[i] = (i, i, eq[i])
            last_node = variables[eq[i]]

    for i in range(len(brackets)):
        build_tree(brackets[i][2], brackets[i][0], brackets[i][1] + 1)
        last_node = variables[brackets[i][2]]

    for k in range(2):
        for i in range(len(ops[k])):
            index = ops[k][i]
            m_start, m_end = operands[index - 1][0], operands[index + 1][1]
            b_serial_no += 1
            var_name = str(b_serial_no)
            left_operand = variables[operands[index - 1][2]]
            right_operand = variables[operands[index + 1][2]]
            new_node = Node(eq[index])
            new_node.attach(left_operand, right_operand)
            variables[var_name] = new_node
            operands[m_start] = (m_start, m_end, var_name)
            operands[m_end] = (m_start, m_end, var_name)
            last_node = new_node

    variables[var] = last_node


def postorder(node: Node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end='')


eq = list(input().strip())
build_tree('root', 0, len(eq))
root_node = variables['root']

postorder(root_node)
