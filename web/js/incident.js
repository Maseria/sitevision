// Load incidents on page load
var API_ENDPOINT = "https://5uqk927m6e.execute-api.us-east-1.amazonaws.com/prod";

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
                <button class="btn btn-sm btn-danger" onclick="deleteIncident('${data.incidentid}'>Delete</button>
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

  function deleteIncident(incidentId) {
    $.ajax({
      url: `${API_ENDPOINT}?incidentId=${incidentId}`,
      type: 'DELETE',
      success: function () {
        $(`#incident-${incidentId}`).remove();
      },
      error: function () {
        alert("Failed to delete incident.");
      }
    });
  }