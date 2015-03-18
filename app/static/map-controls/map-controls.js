$(document).ready(function(){
  var menuLeft = document.getElementById( 'cbp-spmenu-s1' );
  var showLeft = document.getElementById( 'showLeft' );
  var menuTitle = document.getElementById( 'menuTitle' );
  

  classie.toggle( menuLeft, 'cbp-spmenu-open' );

  $('#menuTitle').click(function() {
    

    classie.toggle( menuLeft, 'cbp-spmenu-open' );
    classie.toggle( menuTitle, 'showLeft-collapsed' );

    if(classie.has( menuTitle, 'showLeft-collapsed' )){
      $('#showLeft').html('&raquo');

      // Hide menu item borders when sidebar menu collapsed
      $( ".cbp-spmenu li" ).each(function() {
        $( this ).css('border-bottom-color', '#222')
      });


    }else{
      $('#showLeft').html('&laquo');

      // Show menu item borders when sidebar menu collapsed
      $( ".cbp-spmenu li" ).each(function() {
        $( this ).css('border-bottom-color', '#258ecd')
      });
    }
  });

  /* Accordion display between menu parent items and their children. */ 
  $( ".cbp-spmenu-vertical-item-parent" ).click(function() {
    var elemId = $(this).attr('id');

    if ( $( ".cbp-spmenu-vertical-item-child#" + elemId ).is( ":hidden" ) ) {
      $( ".cbp-spmenu-vertical-item-child#" + elemId ).slideDown( "fast", function() {
        // Animation complete.
      });
    }else{
      $( ".cbp-spmenu-vertical-item-child#" + elemId ).slideUp( "fast", function() {
          // Animation complete.
      });
    }
  });

  /* Checkbox actions. */
  $('.dump-checkbox').click(function() {
    if(this.value == "markers"){
      toggleDumpMarkers(this.checked);

    }else if(this.value == "heat"){
      toggleDumpHeatMap(this.checked);
    }
  });
  
  $('.route-checkbox').click(function() {
    toggleTruckRoute(this.value, this.checked, 'route');
  });

  $('.route-heat-checkbox').click(function() {
    toggleTruckRoute(this.value, this.checked, 'heat');
  });

});