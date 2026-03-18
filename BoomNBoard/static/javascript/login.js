$("#loginForm").on("submit", function(e) {
    e.preventDefault();
    console.log($("#username").val(), $("#password").val());

    $.ajax({
        url: "/home/loginUser/",
        type: "POST",
        data: {
            username: $("#username").val(),
            password: $("#password").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(response) {
            if (response.success) {
                window.location.href = response.redirect_url;
            } else {
                $("#error").text(response.error);
            }
        }
    });
});

$("#username").on("blur", function() {
    $.ajax({
        url: "/checkUsername/",
        data: { username: $(this).val() },
        success: function(response) {
            if (!response.exists) {
                $("#error").text("Username does not exist");
            }
        }
    });
});