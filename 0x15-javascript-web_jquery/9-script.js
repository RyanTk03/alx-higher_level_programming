$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, status) {
    if (status === 'success') {
      $('div#hello').append(data.hello);
    }
  });
});
