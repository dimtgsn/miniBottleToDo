$('document').ready(function () {
    $('.task-remove').on('click', function () {
        $(this).parent().remove();
    });
    $('.custom-checkbox').on('click', function () {
        $(this).addClass('completed');
        uid = $(this).find("input").attr('data-uid');
        $.get("/api/complete/" + uid);
        setTimeout(() => $(this).find("input").attr('disabled', true), 1000);
    });
    $('.desc-btn').on('click', function () {
        // $(this).hide(1000, function(){
        $(this).css({'display': 'none', 'opacity': '0'});
        // });
        $('.form-control').show(10, function(){
           $('.form-control').css({'display': 'inline-block', 'opacity': '1', 'transition': 'all 1s ease-in-out'});
        });
    });
})
