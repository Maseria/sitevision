// Add your API endpoint here
var API_ENDPOINT = "https://5uqk927m6e.execute-api.us-east-1.amazonaws.com/prod";

// AJAX POST request to save incident data
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
