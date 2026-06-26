import json

with open('evalDataTarget.txt', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('const evaluationData = [')
if start_idx == -1:
    print("Not found")
    exit()

start_idx += len('const evaluationData = ')

brace_count = 0
in_array = False
end_idx = -1

for i in range(start_idx, len(text)):
    if text[i] == '[':
        brace_count += 1
        in_array = True
    elif text[i] == ']':
        brace_count -= 1
        
    if in_array and brace_count == 0:
        end_idx = i
        break

if end_idx != -1:
    array_str = text[start_idx:end_idx+1]
    
    # Fix the corrupted characters
    array_str = array_str.replace('?o', '\\"').replace('??', '\\"').replace('?T', "\\'").replace('?~', '\\"')
    
    with open('test_eval.js', 'w', encoding='utf-8') as f:
        f.write('const data = ' + array_str + ';\nconsole.log(JSON.stringify(data));')
    print("Wrote test_eval.js")
else:
    print("End not found")
