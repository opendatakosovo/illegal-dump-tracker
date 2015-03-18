$(document).ready(function(){
  var menuLeft = document.getElementById( 'cbp-spmenu-s1' );
  var showLeft = document.getElementById( 'showLeft' );

  classie.toggle( menuLeft, 'cbp-spmenu-open' );

  $('#showLeft').click(function() {
    classie.toggle( menuLeft, 'cbp-spmenu-open' );
    classie.toggle( showLeft, 'showLeft-collapsed' );

    if(classie.has( showLeft, 'showLeft-collapsed' )){
      $('#showLeft').html('&raquo');
    }else{
      $('#showLeft').html('&laquo');
    }
  });

});