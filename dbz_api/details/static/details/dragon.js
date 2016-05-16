var $abilities = $('#abilities');



$.get('http://127.0.0.1:8000/api/character_statistics/', function(abilities){
  abilities.forEach(function(ability) {
    var $li = $('<li>');
    $li.text(ability.name)
    $li.appendTo($abilities);
  })
})
