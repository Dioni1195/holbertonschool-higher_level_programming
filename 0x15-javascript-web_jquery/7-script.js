$(function (){
  let $characterDisplayed = $('#character');

  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/people/5/?format=json',
    success: function(character) {
      $characterDisplayed.text(character.name);
    }
  })
});
