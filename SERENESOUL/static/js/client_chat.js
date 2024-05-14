
    var ChatosExamle = {
        Message: {
            add: function (message, time, image,chat) {
                $('#chat').append(
                    '<div class="col-xl-12 p-2">\
                        <div class="h-10 bg-light rounded p-4">\
                            <div class="d-flex align-items-center border-bottom py-3">\
                                '+image+'\
                                <div class="w-100 ms-3">\
                                    <div class="d-flex w-100 justify-content-between">\
                                        <h6 class="mb-0">'+chat+'</h6>\
                                        <small>'+time+'</small>\
                                    </div>\
                                    <span>'+message+'</span>\
                                </div>\
                            </div>\
                        </div>\
                    </div>'
                );
            }
        },
    };

    function sendMessage(message, id) {
        $.ajax({
            url: '/api/send_message/',
            type: 'POST',
            data: {
                'content': message,
                'conversation_id': id,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                response = JSON.parse(response);
                ChatosExamle.Message.add(
                    response[0].fields.content,
                    response[0].fields.created_at.split('T')[1].split('.')[0],
                    '<img class="rounded-circle flex-shrink-0" src="/static/img/conv_logo.png" style="width: 40px; height: 40px;">',
                    'SERENE'
                );
            }
        });
    }

    function getConversation(id) {
        $.ajax({
            url: '/api/get_message/',
            type: 'GET',
            data: {
                'conversation_id': id
            },
            success: function (response) {
                $('#chat').html('');
                response = JSON.parse(response);
                for (var i = 0; i < response.length; i++) {
                    if (i % 2 == 0) {
                        ChatosExamle.Message.add(
                            response[i].fields.content,
                            response[i].fields.created_at.split('T')[1].split('.')[0],
                            '<img class="rounded-circle flex-shrink-0" src="/static/img/user.jpg" style="width: 40px; height: 40px;">',
                            'User'
                        );
                    } else {
                        ChatosExamle.Message.add(
                            response[i].fields.content,
                            response[i].fields.created_at.split('T')[1].split('.')[0],
                            '<img class="rounded-circle flex-shrink-0" src="/static/img/conv_logo.png" style="width: 40px; height: 40px;">',
                            'SERENE'
                        );
                    }
                }
            }
        });
    }

    $(document).ready(function () {
        $('#chat-messages').on('click', 'li.nav-item.nav-link', function () {
            var id = $(this).attr('data-chat-user-id');
            $(this).addClass('active').siblings().removeClass('active');
            $(this).find('.nav-link').removeClass('collapsed');
            $(this).siblings().find('.nav-link').addClass('active');
            localStorage.setItem('chat_id', id);
            getConversation(id);
        });
    });
    
    $(document).on('submit', '#chat_form', function (e) {
        e.preventDefault();

        var input = $(this).find('input[type=text]');
        var message = input.val();
        message = $.trim(message);
  
        if (message) {
            ChatosExamle.Message.add(
                    message, 
                    new Date().toLocaleTimeString(),
                    '<img class="rounded-circle flex-shrink-0" src="/static/img/user.jpg" style="width: 40px; height: 40px;">',
                    'User'
                );
            sendMessage(message, localStorage.getItem('chat_id'));
            input.val('');
        } else {
            input.focus();
        }
    });


$(document).ready(function () {

    }
);