var $characters = $('#character');
var $power_level = $('#power_level');
var $card = $(".card")

$.get('http://127.0.0.1:8000/api/character_statistics/', function(characters){
  characters.forEach(function(character) {
    var $p = $('<li>');
    var $p2 = $('<p>');

    $name = character.name
    // $p.text(character.name);
    // $p.appendTo($characters);
    $power_level = character.power_level
    // $p2.text(character.power_level);
    // $p2.appendTo($characters);
    $(".card").append('<div class="stats"> '+ $name + "<br />" + $power_level + '</div>')

  })
})


$( "li" ).first().hide();

// my_list = $.get('http://127.0.0.1:8000/api/character_statistics/', function(response) {
//   console.log(response.data)
// })
// console.log(my_list)



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
