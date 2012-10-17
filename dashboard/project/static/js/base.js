var analyze = $('.analyze');

analyze.on('click', function(){
    analyze.attr('disabled', 'disabled');
    $.get('analyze/', function(context){
        analyze.removeAttr('disabled');
    });
    
});