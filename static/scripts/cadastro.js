//Fazendo um buscar para a tabela CadastroCliente
    var Input_busca = document.getElementById('input-busca')
    var Tabela_Cadastro= document.getElementById('tabelaCadastro')

//cAPTURA O EVENTO QUE FOI FEITO E O VALOR
Input_busca.addEventListener('keyup', () =>{
    
  //Capturando as teclas digitadas
  let expressao = Input_busca.value.toLowerCase()

  //Caputurando as linhas (TAGS) TR
  let linhas = Tabela_Cadastro.getElementsByTagName('tr')
 
  //Pecorrer linhas por linhas
  for(let posicao in linhas)
    {
        //Confere se ta retornando so numero
      if (true === isNaN(posicao)){
        continue
      }

      //diz a posicao que esta a linha pesquisada
      let conteudoDaLinha = linhas[posicao].innerHTML.toLowerCase()

      // compara a se o que tem na expressao exite em alguma parte do tr
      if(true === conteudoDaLinha.includes(expressao)){
        //se tiver mostra aonde ta, deixa essa linha block
        linhas[posicao].style.display = '';
      }else{
        // o restante que nao tiver deixa none, para nao ser exibido
        linhas[posicao].style.display = "none"
      }
    }

})

// 

// function idButton(acao){
//       $( "#dialog-modal" ).dialog({
//           width:850,
//           height: 700,
//           modal: true,
//         });
//   $.ajax({
//       url:"http://127.0.0.1:5000/tabelaCadastro/"+ acao,
//       method:"GET",
//       async:false,
//       success:function(resultado){
//           $('#dialog-modal').html(resultado)
          
//           $('#enviar').click(function(e){
//             console.log("to antes do ajax");
//             var formDados = $('#form').serialize()
//             $.ajax({
//               url: "http://127.0.0.1:5000/tabelaCadastro/{{usuario[0]}}" ,
//               method:"POST",
//               data: formDados,
//               processData:false,
//               async:true,
//               cache:false,
//               dataType:'json',
//               async:false,
//               success:function(data){
//                   alert('Cadastrado com sucesso!');
//                   $("input").val("");
//               },
//               dataType:'html'
//           });
//           return false;
//             })

//           }
//        })
    
//   }
  

