$(document).ready(function() {
    $('#btn_translate').click(function() {
      const lang = $('#language_code').val();
      const url = `https://www.fourtonfish.com/hellosalut/?lang=${lang}`;
  
      $.get(url, function(data) {
        $('#hello').text(data.hello);
      });
    });
  });
  