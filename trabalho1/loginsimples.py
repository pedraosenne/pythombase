while True:
  try:
      loguin = input("digite seu novo loguin: ")
      senha = input("digite sua nova senha (mínimo 6 caracteres): ")
    
      if len(loguin) < 1:
          print("Login não pode estar vazio.")
      elif len(senha) < 6:
          print("Senha deve ter no mínimo 6 caracteres.")
      else:
          print("Login e senha cadastrados com sucesso!")
          break
  except ValueError:
      print("Ocorre um erro inesperado. Por favor, tente novamente.")




print("loguin cadastrado:", loguin)
print("senha cadastrada:", senha)


