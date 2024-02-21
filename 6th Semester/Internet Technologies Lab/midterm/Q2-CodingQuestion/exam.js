$(document).ready(function() {
    var dl=5;
    var st=5;
    var dip=5
    $('.dl').click(function(){
        dl=dl+1;
        console.log(dl)
    });
    $('.st').click(function(){
        st=st+1;
        console.log(st)
    });
    $('.dip').click(function(){
        dip=dip+1;
        console.log(dip)
    });
    $('.SubmitButton').click(function(){
        $('.voteTitle').text('VOTE RESULTS');
        $('.deeplearning').text('Deep Learning: ');
        $('.dlresults').text(dl);
        $('.software').text('Software testing and analysis: ');
        $('.stpresults').text(st);
        $('.digital').text('Digital Image Processing: ');
        $('.dipresults').text(dip);
        if(dl<10)
        {
            $('.notoff1').text('Deep learning is not offered this semester');
        }
        if(st<10)
        {
            $('.notoff2').text('Software testing is not offered this semester');
        }
        if(dip<10)
        {
            $('.notoff3').text('digital image processing is not offered this semester');
        }
    })
});