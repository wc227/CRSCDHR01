$(function(){
    $('#post_con').delegate('span', 'mouseenter', function(){

        $(this).parent().children('span:first').click(function(){
            $(this).addClass('hidden').next().removeClass('hidden').next().removeClass('hidden');
        });

        $(this).parent().children('span:last').click(function(){
            $(this).addClass('hidden').prev().addClass('hidden').prev().removeClass('hidden');
        });
    });


});
