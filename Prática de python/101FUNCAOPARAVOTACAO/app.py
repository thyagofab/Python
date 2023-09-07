def vota(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    return idade

print("--"*35)
nascimeto = int(input("Em que ano você nasceu ?  "))


if vota(nascimeto) < 16:
    print(f"COM {vota(nascimeto)} ANOS: NÃO VOTA.")
elif 16 <= vota(nascimeto) < 18 or vota(nascimeto) > 65:
    print(f"COM {vota(nascimeto)} ANOS: VOTO É OPCIONAL.")
else:
    print(f"COM {vota(nascimeto)} ANOS: VOTO OBRIGATÓRIO")

" OUTRA FORMA DE FAZER: "

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'COM {idade} ANOS: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'COM {idade} ANOS: VOTO OPCIONAL.'
    else:
        return f'COM {idade} ANOS: VOTO OBRIGATÓRIO.'

nasc = int(input("EM QIE ANO VOCÊ NASCEU? "))
print(voto(nasc))
