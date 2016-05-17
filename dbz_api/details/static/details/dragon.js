var $characters = $('.card');
var $power_level = $('#power_level');


$.get('http://127.0.0.1:8000/api/character_statistics/', function(characters){
  characters.forEach(function(character) {
    var $p = $('<li>');
    var $p2 = $('<p>');


    $p.text(character.name);
    $p.appendTo($characters);

    $p2.text(character.power_level);
    $p2.appendTo($characters);
  })
})

$( "li" ).first().hide();

// $.get('http://127.0.0.1:8000/api/character_statistics/'), function(list_characters){
//   list_characters.forEach(function(list_characters) {
//
//   })
// };


// for (i = 0; i < my_list.length; i++) {
//     console.log(my_list);
// }


// var x = myFunction(4, 3);        // Function is called, return value will end up in x
//
// function myFunction(a, b) {
//     return a * b;                // Function returns the product of a and b
// }
