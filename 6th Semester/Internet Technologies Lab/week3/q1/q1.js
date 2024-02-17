$(document).ready(function(){
    $('.btn').click(function(){
        var txt=$('.btn').text()
        if(txt=='CLICK TO MOVE RIGHT'){
            $('.btn').text('CLICK TO MOVE LEFT');
            $('.container').animate({
            left:'500px'
        });
        }
        else if(txt=='CLICK TO MOVE LEFT'){
            $('.btn').text('CLICK TO MOVE RIGHT');
            $('.container').animate({
            left:'0px'
        });
        }
    })
});