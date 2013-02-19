;(function ($, window, undefined) {
  'use strict';

  var $doc = $(document),
      Modernizr = window.Modernizr;

  $(document).ready(function() {
    $.fn.foundationAlerts           ? $doc.foundationAlerts() : null;
    $.fn.foundationButtons          ? $doc.foundationButtons() : null;
    $.fn.foundationAccordion        ? $doc.foundationAccordion() : null;
    $.fn.foundationNavigation       ? $doc.foundationNavigation() : null;
    $.fn.foundationTopBar           ? $doc.foundationTopBar() : null;
    $.fn.foundationCustomForms      ? $doc.foundationCustomForms() : null;
    $.fn.foundationMediaQueryViewer ? $doc.foundationMediaQueryViewer() : null;
    $.fn.foundationTabs             ? $doc.foundationTabs({callback : $.foundation.customForms.appendCustomMarkup}) : null;
    $.fn.foundationTooltips         ? $doc.foundationTooltips() : null;
    $.fn.foundationMagellan         ? $doc.foundationMagellan() : null;
    $.fn.foundationClearing         ? $doc.foundationClearing() : null;

    $.fn.placeholder                ? $('input, textarea').placeholder() : null;


    //Orbit
    $(".hero").orbit({
       'animation' : 'fade'
      ,'timer' : false
      ,'advanceSpeed' : '5000'
      ,'bullets' : true
      ,'captions' : false
      ,'directionalNav' : true
      ,'fluid' : '16x7'
    });

    //Temporarily show signup modal
    $('#signupModal-3')
    .reveal();


    //Modal scroll position fix
    $('[data-reveal-id]')
    .on('click', function(){
      $(window).scrollTop(0);
    });

    //Circular progress bar
    $(".dream-time-progress")
    .knob({
      change : function (value) {
          //console.log("change : " + value);
          return false;
      }
      // release : function (value) {
      //     //console.log(this.$.attr('value'));
      //     //console.log("release : " + value);
      // },
      // cancel : function () {
      //     //console.log("cancel : ", this);
      // },
      ,fgColor : '#56d4c8'
      ,bgColor : '#000000'
      // ,draw : function () {
      // }
    });


  // //Selection containers
  var $selectionContainers = $("[data-selection]");
      $selectionContainers
      .each(function () { 

        var $container = $(this),
            $items = $container.find($container.attr("data-selection")),
            $name = $container.find($container.attr("data-selection-name")),
            itemTotal = $items.length - 1;

          $items
          .on('click',function(){

            var $this = $(this),
                attr = $this.attr('data-selected');

            if (!$this.attr('data-multiple-selection')) {
              $items.removeAttr('data-selected');

            }

            if (typeof attr !== 'undefined' && attr !== false) {
                $this.removeAttr('data-selected');
            } else {
              $this.attr('data-selected','');
            }

          });
      });


  // UNCOMMENT THE LINE YOU WANT BELOW IF YOU WANT IE8 SUPPORT AND ARE USING .block-grids
  // $('.block-grid.two-up>li:nth-child(2n+1)').css({clear: 'both'});
  // $('.block-grid.three-up>li:nth-child(3n+1)').css({clear: 'both'});
  // $('.block-grid.four-up>li:nth-child(4n+1)').css({clear: 'both'});
  // $('.block-grid.five-up>li:nth-child(5n+1)').css({clear: 'both'});

  // Hide address bar on mobile devices (except if #hash present, so we don't mess up deep linking).
  if (Modernizr.touch && !window.location.hash) {
    $(window).load(function () {
      setTimeout(function () {
        // At load, if user hasn't scrolled more than 20px or so...
  			if( $(window).scrollTop() < 20 ) {
          window.scrollTo(0, 1);
        }
      }, 0);
    });
  }

})(jQuery, this);
