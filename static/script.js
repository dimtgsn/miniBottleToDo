$('document').ready(function () {
    $('.task-remove').on('click', function () {
        $(this).parent().remove();
    });
    $('.custom-checkbox').on('click', function () {
        $(this).addClass('completed');
        setTimeout(() => $(this).find("input").attr('disabled', true), 1000);
    });
})
