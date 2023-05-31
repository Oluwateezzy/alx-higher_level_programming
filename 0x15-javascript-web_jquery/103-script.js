$(document).ready(function() {
  $('#btn_translate').click(fetchTranslation);
    
  $('#language_code').keypress(function(event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + languageCode, function(data) {
      const helloTranslation = data.hello;
      $('#hello').text(helloTranslation);
    });
  }
});
