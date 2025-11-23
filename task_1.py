total_minutes = '1h 45m,360s,25m,30m 120s,2h 60s'

result = 0

for minutes in total_minutes.split(','):
    for i in minutes.split():
        if 'h' in i:
            value = int(i.replace('h', ''))
            result += value * 60
        elif 'm' in i:
            value = int(i.replace('m', '')) 
            result += value  
        elif 's' in i:
            value = int(i.replace('s', '')) 
            result += value / 60    

print(result)               