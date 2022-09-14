# import json
# conf_file = "data\conf_matrix.json"
# with open(conf_file, 'r') as fp:
#     conf_matrix = json.load(fp)
        
# mydict = {}
# for i in range(26):
#     mydict[chr(ord('a')+i)] = []

# for key in conf_matrix.keys():
#     for ch in conf_matrix[key]:
#         mydict[ch].append(key)

# print(mydict)         

start_state = "Hello world"
temp = list(start_state)
# new_state = start_state
# new_state.replace(i, ch)
temp[4] = 'i'
new_state = "".join(temp)

print(new_state)