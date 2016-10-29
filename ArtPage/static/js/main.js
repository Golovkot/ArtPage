$(document).ready(function() {
    $("#submit-form").submit(function() {
        var form = $(this);
        var error = false;
        var data = form.serialize();
        $.ajax({
            type: 'POST',
            url: '/Feedback',
            dataType: 'json',
            data: data,
            success: function(data) {
                $('#submit-form')[0].reset();
                alert('Ваше сообщение отправлено!');
            },
        });
        return false;
    });
});  