$(document).ready(function(){

    let $btn = $('.section-1 .button-area button a');


    $btn.click(function(e){
        $('.section-1 .button-area button a').removeClass('active');
        e.target.classList.add('active');
        
        let selector = $(e.target).attr('data-filter');
        $('.section-1 .grid').isotope({
            filter : selector
        });

        return false;
    });

    $('.section-1 .button-area button #btn-1').trigger('click');
});
