var ChatosExamle = {
    Message: {
        add: function (message, time, chat) {
            $('#chat').append(
                '<div class="col-xl-12 p-2">\
                    <div class="h-10 bg-light rounded p-4">\
                        <div class="d-flex align-items-center border-bottom py-3">\
                            <img class="rounded-circle flex-shrink-0" src="./img/user.jpg" style="width: 40px; height: 40px;">\
                            <div class="w-100 ms-3">\
                                <div class="d-flex w-100 justify-content-between">\
                                    <h6 class="mb-0">Jhon Doe</h6>\
                                    <small>15 minutes ago</small>\
                                </div>\
                                <span>Short message goes here...</span>\
                            </div>\
                        </div>\
                    </div>\
                </div>'
            );
        }
    },
};

$(document).ready(function () {
    var chat = $('#chat');
    ChatosExamle.Message.add('Hello, how can I help you?', '10:00 AM', chat);
    ChatosExamle.Message.add('I am looking for the best admin template. Could you please help me to find it out?', '10:01 AM', chat);
    ChatosExamle.Message.add('Absolutely! I can help you with that. I am very familiar with the best admin template. I will help you to find it out.', '10:01 AM', chat);
}
);