// Add your API endpoint here
var API_ENDPOINT = "https://5uqk927m6e.execute-api.us-east-1.amazonaws.com/prod";

// AJAX POST request to save student data
document.getElementById("saveIncident").onclick = function(){
    const incidentid = String(Math.floor(Math.random() * 1000)); // Random
    
    var inputData = {
        "incidentid": incidentid,
        "title": $('#title').val(),
        "date": $('#date').val(),
        "description": $('#description').val()
    };
    console.log(inputData);
    $.ajax({
        url: API_ENDPOINT,
        type: 'POST',
        data:  JSON.stringify(inputData),
        contentType: 'application/json; charset=utf-8',
        success: function (response) {
            document.getElementById("incidentSaved").innerHTML = "Incident Data Saved";
            console.log("We saved the data")
        },
        error: function () {
            alert("Error saving student data.");
        }
    });
}
// Load incidents on page load
$(document).ready(function() {
    $.ajax({
      url: API_ENDPOINT,
      type: 'GET',
      contentType: 'application/json; charset=utf-8',
      success: function (response) {
        $('#incidentList').empty();
        jQuery.each(response, function(i, data) {
          $('#incidentList').append(`
            <div class="col-md-10 col-lg-8 mb-3">
              <div class="border rounded p-3 bg-white shadow-sm">
                <div class="d-flex justify-content-between">
                  <strong>${data.title}</strong>
                  <small class="text-muted">${data.date}</small>
                </div>
                <p class="mb-0 text-muted">${data.description}</p>
              </div>
            </div>
          `);
        });
      },
      error: function () {
        $('#incidentList').html("<p class='text-danger'>Error loading incidents.</p>");
      }
    });
  });