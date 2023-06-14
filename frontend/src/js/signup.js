$(document).ready(function () {
  function showFlashMessage (type, content) {
    const flashMessagesContainer = $('#flash-messages');
    const flashMessage = $(`<div class="${type}">${content}</div>`);
    flashMessagesContainer.html(flashMessage);

    // Automatically hide the flash message after 3 seconds
    setTimeout(function () {
      flashMessage.fadeOut('slow', function () {
        flashMessage.remove();
      });
    }, 3000);
  }

  function sendSignUpData (data) {
    $.ajax({
      type: 'POST',
      url: 'http://localhost:5000/signup',
      headers: {
        'Content-Type': 'application/json'
      },
      data: JSON.stringify(data),
      success: function (response) {
        console.log(response);
        showFlashMessage('success', response.message);
      },
      error: function (xhr, textStatus, errorThrown) {
        if (xhr.status === 418) {
          // console.log("The User already exists.");
          showFlashMessage('error', 'User with that email already exists');
        } else if (xhr.status === 500) {
          showFlashMessage('error', 'Internal Server Error, try again');
        } else {
          showFlashMessage('error', 'An error occurred, try again later');
        }
      }
    });
  }

  $('#signup-form').submit(function (e) {
    e.preventDefault();

    const email = $('#email').val();
    const name = $('#name').val();
    const password = $('#password').val();

    const data = {
      email: email,
      name: name,
      password: password
    };

    console.log(JSON.stringify(data));
    sendSignUpData(data);
  });
});
