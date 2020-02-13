$(function (){
  let $hello = $('#hello');

  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (trans) {
      $hello.text(trans.hello);
    }
  });
});
