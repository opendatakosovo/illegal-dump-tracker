$(document).ready(function(){
  var menuLeft = document.getElementById( 'cbp-spmenu-s1' );
  var showLeft = document.getElementById( 'showLeft' );

  classie.toggle( menuLeft, 'cbp-spmenu-open' );

  showLeft.onclick = function() {
    classie.toggle( this, 'active' );
    classie.toggle( menuLeft, 'cbp-spmenu-open' );
  };

});