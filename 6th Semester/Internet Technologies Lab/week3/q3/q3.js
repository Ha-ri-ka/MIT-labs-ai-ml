$('document').ready(function(){
    $('.update').click(function(){
        var color=$('#colors').val()
        if(color)
        {$('.card').css('background-color',color);}
        var fontStyle=$('#fonts').val();
        if(fontStyle)
        {$('.messageText').css('font-family',fontStyle);}
        var fontSize=$('#size').val();
        if(fontSize)
        {$('.messageText').css('font-size',Number(fontSize));}
        var border=$('input[name="border"]:checked').val()
        if(border)
        {$('.card').css('border',border);}
        var isChecked = $('#picChoice').is(':checked');
        if(!isChecked)
        {
            $('.picture').remove();
        }
        var message=$('.txt').val();
        $('.messageText').text(message);
        
    })
})