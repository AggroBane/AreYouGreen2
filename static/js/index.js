$(document).ready(function()
{
    $('#log').append('<p>AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</p>');

    var socket = io();

    $('#log').append('<p>Socket started</p>');

    socket.on('my response', function(msg) 
    {
        $('#log').append('<p>Received: ' + msg.data + '</p>');
    });
});