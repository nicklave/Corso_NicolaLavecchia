# Scrivete un programma che utilizza una funzione che accetta
# come parametro una stringa passata dall’utente e restituisce in
# risposta se è palindroma o no.
# Esempio:
# ‘I topi non avevano nipoti’ è palindroma
# 'ciao' non è palindroma



def palindroma(s):
    s1 = ''
    for char in s[::-1]:
        s1+=char
    if s1 == s:
        return True
    return False

print(palindroma('anna'))
print(palindroma('nicola'))
print(palindroma('itopinonavevanonipoti'))
