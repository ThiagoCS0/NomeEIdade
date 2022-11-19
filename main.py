def ini():
  anoOk=False
  nomeOk=False
  while (not nomeOk):
    nome=input ("Nome completo:")
    if len(nome)<4:
      print("\nERRO:\nDigite o nome completo\n")
    else:
      nomeOk=True
      
  while (not anoOk):
    try:
      ano=int(input ("Ano de nascimento:"))
      if len(str(ano)) == 4:
        if 2023>ano>1921:
          anoOk=True
        else:
          print ("\nERRO:\nDigite um ano válido, de 1922 até 2022\n")
      else:
        print("\nERRO:\nDigite os 4 números referentes ao ano.\nExemplo: 1990\n")

    except:
      print("\nERRO:\nDigite apenas números em \"Ano de nascimento\"\nExemplo: 1990\n")
  print ("\n\nSeu nome:",nome)
  print ("Sua idade:",str(2022-ano) + " anos")
ini()