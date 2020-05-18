$(document).ready(function() {
  $(".error").hide();
  $("#calculate").click(function(e) {
    e.preventDefault();
    var data = {
      a: {
        lat: $("#a-lat").val(),
        lon: $("#a-lon").val()
      },
      b: {
        lat: $("#b-lat").val(),
        lon: $("#b-lon").val()
      }
    };
    $.ajax({
      url: "/distance/",
      method: "POST",
      data: JSON.stringify(data),
      contentType: "application/json",
      format: "json",
      success: function(result) {
        $("#distance").html(result["distance"]);
        $("#result").show();
      },
      error: function(error) {
        $(".error").html("Error occured.")
        $(".error").show();
      }
    });
  });
});
