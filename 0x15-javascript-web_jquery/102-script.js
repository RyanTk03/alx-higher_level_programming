$(function () {
  $('input#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data, status) {
      if (status === 'success') {
        // Using html instead of text to handle of many language
        $('div#hello').html(data.hello);
      }
    });
  });
});
