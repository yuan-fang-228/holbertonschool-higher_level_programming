document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://stefanbohacek.com/hellosalut/?lang=';
    const language = $('INPUT#language_code').val();
    $.get(url + language, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
