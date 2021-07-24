function autorefresh() {
    // auto refresh page after 2 seconds
    setInterval('refreshPage()', 2000);
}

function refreshPage() {
    $.ajax({
    url: '{% url "game:table" %}',
    success: function(data) {
    $('#console').html(data);
    }
});
}