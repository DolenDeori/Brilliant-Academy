
// dynamic loading map
var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyDzSb9PW9yOJrODdcqUDsPvYWlNeUeCsL0&callback=initMap';
script.async = true;


window.initMap = function() {
    // The location of north lakhimpur
    const northLakhimpur = { lat: 27.23684, lng: 94.0962 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 17,
      center: northLakhimpur,
      // mapTypeId: 'satellite'
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
      position: northLakhimpur,
      map: map,
    });
};

document.head.appendChild(script);
      


// date
var date = new Date();
function datetime(){
  var toDate = date.getDate()
  var month = date.getMonth()
  var year = date.getUTCFullYear()
  var month_list = ['January' , 'february' , 'March' , 'April' , 'May' , 'June' , 'July' , 'September' , 'October' , 'November' , 'December']
  document.getElementById('date').innerHTML = toDate
  document.getElementById('Month').innerHTML = month_list[month]
  document.getElementById('year').innerHTML = year
}

datetime();


// owlCarousel
$(document).ready(function(){
  $(".authority").owlCarousel({
    loop:!0,
    autoplay:!0,
    dots:!0,
    responsive:{
      0:{items:1},
      asf700:{items:1},
      900:{items: 1}
    }
  })

  $(".feedback-content").owlCarousel({
    loop:!0,
    autoplay:!0,
    dots:!0,
    responsive:{
      0:{items:1},
      asf700:{items:1},
      1000:{items: 2}
    }
  })
});

//   animate on scroll

AOS.init();