var $characters = $('#character');
var $power_level = $('#power_level');
var $card = $(".card")
var count = 1


$.get('http://127.0.0.1:8000/api/character_statistics/', function(characters){
  characters.forEach(function(character) {

    $name = character.name
    $power_level = character.power_level

    $(".card").append('<div class="stats" id='+count+'> '+ $name + "<br />" + $power_level + '</div>')
    count++
  })
})


$( "li" ).first().hide();
