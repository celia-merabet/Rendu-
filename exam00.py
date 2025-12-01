def longueur_dernier_mot(s: str) -> int:
    s = s.strip()
    mots = s.split()
    return len(mots[-1])

s = input("Entrez une phrase : ")
print(longueur_dernier_mot(s))
