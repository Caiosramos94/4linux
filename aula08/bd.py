from BancoDados import BancoDados

bd = BancoDados()


bd.inciaConexao()

bd.consultaRegistro()

#bd.insereRegistro()
bd.atualizaRegistro()

bd.removeRegistro()

bd.consultaRegistro()
    
bd.conexao.close()
