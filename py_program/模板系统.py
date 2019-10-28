import fileinput, re

#正则表达式匹配括号中字段:
field_pat = re.compile(r'\[(.+?)\]')

scope = {} #收集变量

def replacement(match):
    code = macth.group(1)
    try:
        return str(eval(code, scope))
    except SyntaxError:
        exec(code) in scope
        return ''
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

#将field模式里的所有模式全部匹配掉
print(field_pat.sub(replacement, text))
