// Add your API endpoint here
var API_ENDPOINT = "https://5uqk927m6e.execute-api.us-east-1.amazonaws.com/prod";

// AJAX POST request to save student data
document.getElementById("saveIncident").onclick = function(){
    var inputData = {
        "incidentid": $('#incidentid').val(),
        "title": $('#title').val(),
        "date": $('#date').val(),
        "description": $('#description').val()
    };
    $.ajax({
        url: API_ENDPOINT,
        type: 'POST',
        data:  JSON.stringify(inputData),
        contentType: 'application/json; charset=utf-8',
        success: function (response) {
            document.getElementById("incidentSaved").innerHTML = "Incident Data Saved";
        },
        error: function () {
            alert("Error saving student data.");
        }
    });
}