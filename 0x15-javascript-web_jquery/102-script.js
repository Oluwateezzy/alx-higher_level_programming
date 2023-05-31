$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + languageCode, function(data) {
      const helloTranslation = data.hello;
      $('#hello').text(helloTranslation);
    });
  });
});
