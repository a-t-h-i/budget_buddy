$(document).ready(function() {
    $('#usernameInput').on('keyup', function() {
        var username = $(this).val();
        
      $.ajax({
        url: '/check_username',
        method: 'GET',
        data: { username: username },
        
        success: function(response) {
          $('#usernameCheck').html(response);
          },
        
        error: function(xhr, status, error) {
          console.error("Request failed with status:", status);
        }
      });
    });
});