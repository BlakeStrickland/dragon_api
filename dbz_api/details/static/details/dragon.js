var $abilities = $('#abilities');

$.get('http://127.0.0.1:8000/api/character_statistics/', function(abilities){
  abilities.results.forEach(function(ability) {
    console.log(ability)
    var $li = $('<li>');
    $li.text(ability.ability_name)
    $li.appendTo($abilities);
  })
})
