// Adding a new <li> element to UL.my_list when the user clicks on DIV#add_item using the jQuery API
$(document).ready(function(){
  $('DIV#add_item').on('click', function(){
    $('UL.my_list').append('<li>Item</li>');
  });
});

