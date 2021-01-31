var socket = io(); 

$(document).ready(function()
{
    // Try to join organisation (if he is in it)
    socket.emit('joinOrganisation', orgId, username);

    
    /*socket.on('connection', function() 
    {
        $('#log').append("<p>Vous avez rejoint l'organisation</p>");
    });

    socket.on('newConnection', function(username) 
    {
        $('#log').append("<p>" + username + " a rejoint l'organisation</p>");
    });*/
});