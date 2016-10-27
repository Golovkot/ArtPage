$(function() {
    $(document).on('submit', '#submit-form', function(e) {
        $.ajax({
            url: $(this).attr('action'),
            data: $(this).serialize(),
            type: 'POST',
            success: function(html) {
                $(this).clearForm();
                alert('Ваше сообщение отправлено!')
            },
                    });
    });
    e.preventDefault();
});

  