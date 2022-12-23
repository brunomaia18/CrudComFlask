

function TabelaCadastro(){
    $(document).ready(function(){
        $.ajax({
            url:"http://127.0.0.1:5000/tabelaCadastro",
            method:"GET",
            async:false,
            success: function(resultado){
                $("#info").html(resultado)

            }

        })
    })
}
function cadastroCliente(){
    $(document).ready(function(){
        $.ajax({
            url:"http://127.0.0.1:5000/CadastroCliente",
            method:"GET",
            async:false,
            success:function(resultado){
                $("#info").html(resultado)
           
            }
        })
    })
}

$(document).on('click','#tabelaCadastro td button', function(e){
    e.preventDefault();
    var id_cliente = $(this).parent().attr("id")
    $("#tabelaCadastro caption").text($(this).text());
   console.log(id_cliente); // apenas para verificar o valor
})




$(document).ready(function(){
    $('#btnedit{{x[0]}}').click(function(){
        $( "#dialog-modal" ).dialog({
            width:850,
            height: 700,
            modal: true,
          });
    $.ajax({
        url:"http://127.0.0.1:5000/tabelaCadastro/",
        method:"GET",
        async:false,
        success:function(resultado){
            $('#dialog-modal').html(resultado)
            
            }
         })
     })
})


    