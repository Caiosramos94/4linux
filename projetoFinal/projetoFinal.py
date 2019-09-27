from teste import CadastroUsuario
menu = CadastroUsuario()

menu.inciaConexao()
if menu.exibirMenu() == 2:
    menu.Consultacadastro()
    
   # menu.inserircadastro()
menu.conexao.close()
exit()    

  
    
    
