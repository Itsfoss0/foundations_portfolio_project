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

  $('#login-form').submit(function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const email = $('#email').val();
    const password = $('#password').val();

    const data = {
      email: email,
      password: password
    };

    const headers = {
      'Content-Type': 'application/json',
      'User-Agent': ' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    };

    const jsonData = JSON.stringify(data);

    $.ajax({
      type: 'POST',
      url: 'http://localhost:5000/login',
      data: jsonData,
      headers: headers,
      dataType: 'json',
      success: function (response) {
        localStorage.setItem('tokken', response.tokken);
        showFlashMessage('success', `Welcome ${response.user}`);
        // console.log(response.tokken);
        $('.main-block').hide();
        /*
        GET the tasks for the User and update the UI
        */
        tokken = localStorage.getItem('tokken');
        const taskHeaders = {
          Authorization: `Bearer ${tokken}`,
          'Content-Type': 'application/json',
          'User-Agent': ' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        };
        $.ajax({
          type: 'GET',
          url: 'http://localhost:5000/tasks',
          dataType: 'json',
          headers: taskHeaders,
          success: function (response) {
            $('.main-block').hide();
            response.tasks.forEach(element => {
              // console.log(element.title)
              $('#task-list').append(`
              <div class="task-item">
                <span id=${element.id} class="task-title"><font color="blue">Title: </font>${element.title}</span>
                <span class="task-description">Description: ${element.description}</span>
                <span class="task-date">Due on: ${element.due_date}</span>
                <span class="task-actions">
                  <label class="icon edit-icon"><i class="fas fa-pencil-alt"></i></label>
                  <label class="icon delete-icon"><i class="fas fa-trash-alt"></i></label>
                  <label class="icon check-icon"><i class="fas fa-check"></i></label>
                </span>
              </div>`);
              $('.task-actions .edit-icon').on('click', function () {
                const taskItem = $(this).closest('.task-item');
                const taskId = taskItem.attr('id');
                const taskTitle = taskItem.find('.task-title').text().replace('Title: ', '');
                const taskDescription = taskItem.find('.task-description').text().replace('Description: ', '');
                const taskDueDate = taskItem.find('.task-date').text().replace('Due on: ', '');

                // Set the task details in the edit form
                $('#edit-task-form #edit-task-id').val(taskId);
                $('#edit-task-form #edit-task-title').val(taskTitle);
                $('#edit-task-form #edit-task-description').val(taskDescription);
                $('#edit-task-form #edit-task-due-date').val(taskDueDate);
                // Show the edit form
                $('#edit-task-popup').toggle();
              });
            });
            $('.avatar').text(response.email.at(1).toUpperCase());
            $('#task-section').show();
            $('.avatar').on('click', function () {
              $('#signout-popup').toggle();
            });
            $('#signout-form').submit(function (event) {
              event.preventDefault();
              $('#task-section').hide();
              $('#signout-popup').hide();
              showFlashMessage('success', `Logged out ${response.email}`);
              window.location.href = './login.html';
            });
          }
        });
      },
      error: function (xhr) {
        if (xhr.status === 401) {
          showFlashMessage('error', 'Authentication failed. Please check your credentials.');
        } else {
          showFlashMessage('error', 'An error occurred. Please try again later.');
        }
      }
    });
  });
  // Edit task form event handler from here ->>>
  $('#edit-task-form').submit(function(event) {
    event.preventDefault();
    const taskId = $('#edit-task-id').val();
    const updatedTitle = $('#edit-task-title').val();
    const updatedDescription = $('#edit-task-description').val();
    const updatedDueDate = $('#edit-task-due-date').val();
    const taskItem = $('#' + taskId);
    taskItem.find('.task-title').text('Title: ' + updatedTitle);
    taskItem.find('.task-description').text('Description: ' + updatedDescription);
    taskItem.find('.task-date').text('Due on: ' + updatedDueDate);
    // alert('Stop pocking me')
    $('#edit-task-popup').hide();
    // Additional logic for updating the UI with the new task props
  });
  
});

  
