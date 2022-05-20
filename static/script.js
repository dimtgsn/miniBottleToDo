$('document').ready(function () {
    $(document).on('click', '.task-remove', function () {
        $(this).parent().remove();
    });
    $(document).on('click', '.custom-checkbox-input', function () {
        $(this).next().addClass('completed');
        setTimeout(() => $(this).attr('disabled', true), 1000);
        //uid = $(this).attr('data-uid');
        document.querySelector("#com").click();
        //$.get("/api/complete/" + uid);
    });
    $(document).on('click', '.desc-btn', function () {
        $(this).css({'display': 'none', 'opacity': '0'});
        $('.form-control').show(10, function(){
           $('.form-control').css({'display': 'inline-block', 'opacity': '1', 'transition': 'all 1s ease-in-out'});
        });
    });
})
