s= "aaaabbbbcccc"
array = {}
for i in s:
      if i in array:
            array[i] += 1
      else:
            array[i] = 1

result = []
smallest = True
while array:
      keys = [key for key in array]
      keys = sorted(keys) if smallest else sorted(keys, reverse=True)
      smallest = not smallest
      for key in keys:
            result.append(key)
            if array[key] == 1:
                  del array[key]
            else:
                  array[key] -= 1
print(''.join(result))



