var triptypehash = {
    "Islands and Beaches" : "IslandsBeaches",
    "Immerse Yourself in New Cultures": "ImmersedInNewCultures",
    "Great Cities": "GreatCities",
    "Adventure and Explore": "ExploreAdventure",
    "Do good": "DoGood",
    "Cultural Treasures": "CulturalTreasures"
}

function analytics() {
$('a[data-reveal-id]').click(function () {
    // console.log(['_trackEvent', 'Modal', 'Open', $(this).attr("data-reveal-id")]);
    _gaq.push(['_trackEvent', 'Modal', 'Open', $(this).attr("data-reveal-id")]);
    });
}

function resetSelection(){
  // //Selection containers
  var $selectionContainers = $("[data-selection]");
      $selectionContainers
      .each(function () {

        var $container = $(this),
            $items = $container.find($container.attr("data-selection")),
            $name = $container.find($container.attr("data-selection-name")),
            multipleSelection = $container.attr("data-multiple-selection"),
            itemTotal = $items.length - 1;

          $items
          .on('click',function(){

            var $this = $(this),
                selected = $this.attr('data-selected');

            if (typeof multipleSelection !== 'undefined' && multipleSelection !== false) {

            } else {
              $items.removeAttr('data-selected');
            }

            if (typeof selected !== 'undefined' && selected !== false) {
                $this.removeAttr('data-selected');
            } else {
              $this.attr('data-selected','');
            }

          });
      });
}
function renderModal(){
    var name = $('a[data-selected]').data('selection-value')
    //console.log("Name = " + name );
    template = Mustache.template('activities')
    $('#travelerActivities').html(template.render(Questions[name]))
    resetSelection();
    $('#shareButton').on('click', function(event){ shareme() });
    $("#travelerActivities").reveal()
}

function quizzSummary(){
    var summary = {
        event: $('form#tripType div.custom a.current').text(),
        tripType: $('#travelerType a[data-selected]').data('selection-value'),
        image_letters: []
    }
    $.each( $('#travelerActivities a[data-selected]'),
           function(index, value) {
               summary['image_letters'].push($(value).data('selection-letter'));
           });
    summary['image_url'] = "https://s3.amazonaws.com/assets.dreamfunder.co/share/" + triptypehash[summary['tripType']] + "/" + summary['image_letters'].sort().join('') + ".png"
    return summary
}

function fb_share(event,image_url){
    FB.ui(
      {
       method: 'feed',
       name: 'Dreamfunder',
       caption: 'Your ' + event + ' trip, gifted by your family and friends',
       description: (
           'Tell your friends about your ideas for your dream trip'
       ),
       link: 'http://dreamfunder.co',
       picture: image_url
      },
      function(response) {
        if (response && response.post_id) {
    $('form#reporting').submit();
        } else {
    $('form#reporting').submit();
        }
      }
    );
}

function shareme() {
    $('#travelerActivities').trigger('reveal:close')
    summary = quizzSummary()
    fb_share(summary['event'], summary['image_url'])
    $("form#reporting input[name='report']").val(JSON.stringify(summary))
}
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
      ,'timer' : true
      ,'advanceSpeed' : '4000'
      ,'bullets' : true
      ,'captions' : false
      ,'directionalNav' : true
      ,'fluid' : '16x7'
    });

    analytics();

    //Temporarily show signup modal
    //$('#signupModal-3').reveal();

    //Show the DreamTrip modal based on the anchor
    if (window.location.hash == '#dreamTrip'){
        $('#dreamTrip').reveal();
         _gaq.push(['_trackEvent', 'Modal', 'Open', 'SpecialOccasion']);
         window.location.hash = ''
    }
    //Show the Thanks modal based on the anchor
    if (window.location.hash == '#ThankYou'){
        $('#supporterThanks').reveal();
         window.location.hash = ''
         _gaq.push(['_trackEvent', 'Modal', 'Open', 'ThankYou']);
    }


    // Set the custom actions on the next button
    $('#activateActivities').on('click', function(event){ renderModal() });

    // Reset the pronouns
    $('a[data-reveal-id=supporterEvent]').on('click', function(event) {
            if  ($('form select[name=quiz_relationship]').val() == 'ME'){
                $('span.pronoun').html('Your');
            } else {
                $('span.pronoun').html('Their');
            }
        });
    //Set the selections
    resetSelection();

    // Set the visibility on the extra questions
//    if $('li#OtherOption').hasclass('selected'){
//        $('div#OtherOccasionQuestion').display = 'block';
//    }



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



});


  // UNCOMMENT THE LINE YOU WANT BELOW IF YOU WANT IE8 SUPPORT AND ARE USING .block-grids
   $('.block-grid.two-up>li:nth-child(2n+1)').css({clear: 'both'});
   $('.block-grid.three-up>li:nth-child(3n+1)').css({clear: 'both'});
   $('.block-grid.four-up>li:nth-child(4n+1)').css({clear: 'both'});
   $('.block-grid.five-up>li:nth-child(5n+1)').css({clear: 'both'});

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
