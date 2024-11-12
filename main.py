import random

#Vælger to tilfældige primtal som ingen må kende untagen dig:
p = 499 #Første primtal
q = 1999 #Andet primtal

N = p * q #Her finder vi den primtalsfaktorisering, som bruges til Modulooperatoren i vores nøgler

#Vi kan nu bruge N til at beregne Eulers totient-funktion. Hvilket angiver antallet af psitive heltal mindre end N, der er indbrydes primiske med N.

def Eulers_totient_funktion(p, q):
    return (p-1)*(q-1)

phi_N = Eulers_totient_funktion(p, q)

#Vi skal nu vælge et tal som vi skal bruge til enkryptering, som vi kalder den offentlige eksponent:

#Denne funktion tjekker hvad den største fælles divisor for 2 tal er. Den funktion vil vi gerne bruge til at finde ud af om det tal vi vælger har den største fælles divisor 1.
def __gcd(a, b): 

    # Everything divides 0 
    if (a == 0 or b == 0): return 0
    
    # base case
    if (a == b): return a
    
    # a is greater
    if (a > b): 
        return __gcd(a - b, b)
            
    return __gcd(a, b - a)

#For at finde vores offentlige eksponet generere jeg tilfældige tal indtil dens største fælles divisor med phi_N er 1. 
e = random.randint(2, phi_N - 1)
while __gcd(e, phi_N) != 1:
    e = random.randint(2, phi_N - 1)

#Vi har nu fundet vores offentlige nøgle som folk kan bruge til at enkryptere deres beskeder med: (e, N)
#Det næste vi skal er at finde d, altså dekrypterings nøglen.

def modulære_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d

d = modulære_inverse(e, phi_N)

#Vi har nu vores dekrypterings nøgle, som vi skal beholde hemmeligt.
#Disse to nøgler er nu matematisk forbundet, så den ene kan enkryptere og kun den anden nøgle kan dekryptere beskeder.

#Hvordan bruger man nøglerne:

def enkryptering(besked, e, N):
    enkodet_besked = [ord(c) for c in besked] #Omskriver beskeden til Unicode. Altså fra bukstaver til tal
    enkrypteret_besked = [pow(c, e, N) for c in enkodet_besked] #Tager vores enkodet_besked og opløfter den i e og modulooperatoren N.
    return enkrypteret_besked 

def dekryptering(besked, d, N):
    enkodet_besked = [pow(c, d, N) for c in besked]
    bukstavs_besked = [chr(c) for c in enkodet_besked]
    return bukstavs_besked


bukstavs_besked = "RSA-enkryptering"

enkrypteret_besked = enkryptering(bukstavs_besked, e, N)
print(f"\nOffentlige Eksponent: {e} og Modulooperator: {N}")
print(enkrypteret_besked)

print(f"\nPrivate Eksponent: {d} og Modulooperator: {N}")
dekrypteret_besked = dekryptering(enkrypteret_besked, d, N)
print("".join(dekrypteret_besked))
