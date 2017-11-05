
function showDonationForm() {
    document.getElementById("formTitle").innerHTML="Add A Donation";
    document.getElementById("deliveryInput").style.display = "block";
    document.getElementById("itemLabel").textContent="Item to donate* (required)";
    document.getElementById("pickupInput").style.display = "none";
    document.getElementById("displayForm").style.display = "block";
    document.getElementById("formtype").value = "donate";
    //document.getElementById("datelabel").textContent="Drop Off Date";
    document.getElementById("location").required = true;
    document.getElementById("locationlabel").textContent= "Address* (required)";
    document.getElementById("location").placeholder = "Enter your address or location of pickup";
    document.getElementById("item").placeholder= "Enter the item to donate";
    
}

function showRequestForm() {
    document.getElementById("formTitle").innerHTML="Add A Request";
    document.getElementById("itemLabel").textContent="Item requested* (required)";
    document.getElementById("pickupInput").style.display = "block";
    document.getElementById("deliveryInput").style.display = "none";
    document.getElementById("formtype").value = "request";
    document.getElementById("displayForm").style.display = "block";
    //document.getElementById("datelabel").textContent="Pickup Date";
    document.getElementById("location").required = false;
    document.getElementById("locationlabel").textContent= "Address";
    document.getElementById("location").placeholder = "Enter your address or location of dropoff";
    document.getElementById("item").placeholder = "Enter the item to request";
}

// initialize current time
$(function(){  
  $('input[type="time"][value="now"]').each(function(){    
    var d = new Date(),        
        h = d.getHours(),
        m = d.getMinutes();
    if(h < 10) h = '0' + h; 
    if(m < 10) m = '0' + m; 
    $(this).attr({
      'value': h + ':' + m
    });
  });
});
