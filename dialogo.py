print ("Bom dia, como você está hoje")
#sempre ao iniciar o sistema ou app
resposta_usuário=str(input("responda aqui "))
#primeira resposta do usuário 

if  resposta_usuário==("estou bem","tudo bem","tudo otimo","tudo numa nice"):
    #tentar prever as varias possíveis resposta dadas pelo usuário  
    print ("fico feliz por você estar bem")
    #resposta do sistema tentando responder essa questão
   
if resposta_usuário==("mais ou menos","já estive melhor","não estou bem"):
     print ("Gostaria de conversa?") 
     resposta_usuário=str(input("responda aqui: "))

if resposta_usuário!=("sim","gostaria","pode ser"):
     print ("O que aconteceu?,sou todo ouvidos")






