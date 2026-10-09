## Avaliação pratica
1)	Autocommit: É quando as alterações são salvas automaticamente. O padrão recomendado é False para permitir controlar as transações e confirmar as alterações com commit()
2)	db.add() e db.commit(): add() adiciona o objeto à sessão, enquanto commit() salva as alterações no banco. Se chamar commit() antes, apenas confirma as alterações pendentes naquele momento.
3)	'__tablename __': Define o nome da tabela no banco. A chave estrangeira (ForeignKey) precisa referenciar o nome correto da tabela e da coluna para estabelecer o relacionamento.
4)	String(60): Define um limite de tamanho de 60 caracteres. Usar apenas String não especifica esse limite, o que pode dificultar a validação dos dados.
5)	Arquivo .db: É o arquivo que armazena os dados do banco SQLite. Se deletá-lo e executar main.py novamente, o banco poderá ser recriado, mas os dados antigos serão perdidos.
