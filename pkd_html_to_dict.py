options = []

with open('./source.html') as file:
    prev = None
    i = 0
    for line in file:
        if '<td style="text-align: center;"><a href="/wyszukiwarka/pkd' in line.strip():
            prev = line.strip()[len(line.strip())-20:len(line.strip())-9]
        elif '<td><a href="/wyszukiwarka/pkd/' in line.strip():
            options.append((prev, line.strip()[46:-9]))
            prev = None

print(options)
