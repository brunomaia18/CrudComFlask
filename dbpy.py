import pymysql as pydb
import json
class BancoDeDados:
        mydb = pydb.connect(
        host="localhost",
        user="root",
        password="",
        database="database",autocommit=True
    )

        mycursor = mydb.cursor()
        
        # def selectCadastroCliente(self):
        #         self.mycursor.execute("SELECT * FROM cadastro")
        #         self.myresult =  self.mycursor.fetchall()
                
        #         return self.myresult
        
        def selectCadastroCliente(self):
                self.mycursor.execute("SELECT * FROM cadastro")
                self.myresult =  self.mycursor.fetchall()
                lista = list()
                for x in self.myresult:
                        lista.append(
                                {
                        "id":x[0],
                        "Vendedor":x[1],
                        "Cliente":x[2],
                        "Telefone":x[3],
                        "Cidade":x[4],
                        "Bairro":x[5],
                        "Endereco":x[6],
                        "Meio":x[7],
                        "Codigo":x[8],
                        "Quantidade":x[9],
                        "Venda":x[10],
                        "Entrega":x[11],
                        "Valor":x[12],
                        "Pagamento":x[13],
                        "Obs":x[14]
                                })
                return lista



        def inserirCadastroCliente(self,vendedor,cliente,telefone,cidade,bairro,endereco,meio,codigo,quantidade,venda,entrega,valor,pagamento,obs):
                val = (vendedor,cliente,telefone,cidade,bairro,endereco,meio,codigo,quantidade,venda,entrega,valor,pagamento,obs)
                sql  = f"INSERT INTO cadastro(vendedor,cliente,telefone,cidade,bairro,endereco,meio,codigo,quantidade,venda,entrega,valor,pagamento,obs) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                self.mycursor.execute(sql,val)
                self.mydb.commit()
                print(self.mycursor.rowcount,"DEU CERTO")
                
        def selectUserID(self,id):
                self.mycursor.execute(f"SELECT * FROM cadastro where id = {id}")
                self.myresult =  self.mycursor.fetchall()
               
                nmId = self.myresult[0][0]
                vendedor = self.myresult[0][1]
                cliente = self.myresult[0][2]
                telefone = self.myresult[0][3]
                cidade = self.myresult[0][4]
                bairro = self.myresult[0][5]
                endereco = self.myresult[0][6]
                meio = self.myresult[0][7]
                codigo = self.myresult[0][8]
                quantidade = self.myresult[0][9]
                venda = self.myresult[0][10]
                entrega = self.myresult[0][11]
                valor = self.myresult[0][12]
                pagamento = self.myresult[0][13]
                obs = self.myresult[0][14]
                return nmId,vendedor,cliente,telefone,cidade,bairro,endereco,meio,codigo,quantidade,venda,entrega,valor,pagamento,obs,

        def UpdateTabelaCadastro(self,id,vendedor,cliente,telefone,cidade,bairro,endereco,meio,codigo,quantidade,venda,entrega,valor,pagamento,obs):
                self.mycursor.execute(f"UPDATE cadastro SET vendedor=%s,cliente =%s , telefone=%s, cidade = %s, bairro = %s, endereco = %s, meio = %s, codigo = %s, quantidade = %s, venda =%s, entrega =%s, valor =%s, pagamento =%s, obs =%s   WHERE id = %s ",(vendedor,cliente,telefone,cidade,bairro,endereco,meio,codigo,quantidade,venda,entrega,valor,pagamento,obs,id))
                self.mydb.commit()
                
                print(self.mycursor.rowcount,"DEU CERTO")

                
p1 =BancoDeDados()
p1.UpdateTabelaCadastro(23,"Bruninho","FernandaTElesRibeiro","999","fortal","meireles","rua20","insta","bolo","1","2022-11-02","2022-11-02","12","avista","teste")