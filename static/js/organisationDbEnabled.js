$(document).ready(function()
{
    currentTab = 0;
    tempData = JSON.parse(tempData);

    Object.keys(tempData).forEach(tab => {
        var tabElem = document.createElement("div");
        tabElem.appendChild(document.createTextNode(tab));
        tabElem.id = tab;
        
        document.getElementById("tabs").appendChild(tabElem);
        
        console.log(tab);

        tabElem.addEventListener("click", function() {
            loadTab(tab);
        });
    });

    loadTab(Object.keys(tempData)[0]);

    document.getElementById("chatMinimize").addEventListener("click", function() {
        chat = $("#chat");

        if (chat.height() < 100)
        {
            chat.animate({ "height": "30%", "width": "30%" }, 600, function() {
                chat.toggleClass("chatMinSize");
                $("#chatMinimize").text('➖');
                $('#chatBody').show();
            });
        }
        else
        {
            chat.toggleClass("chatMinSize");
            chat.animate({ "height": "40", "width": "170" }, 600, function() {
                $("#chatMinimize").text('➕');
                $('#chatBody').hide();
            });
        }
    });
});

function loadTab(tabId) {
    if (currentTab != tabId)
    {
        $('#' + currentTab).removeClass("curTab");
    }

    currentTab = tabId;

    $('#' + currentTab).addClass("curTab");

    tasks = document.getElementById("tasks");
    tasks.innerHTML = "";

    Object.keys(tempData[tabId]).forEach(task => {
        var taskChkbox = document.createElement("input");
        taskChkbox.type = "checkbox";
        taskChkbox.checked = tempData[tabId][task][0];
        taskChkbox.id = "chk" + task;

        var taskLabel = document.createElement("label");
        taskLabel.appendChild(document.createTextNode(task));
        //taskLabel.htmlFor = "chk" + task; --> block check by clicking on label
        taskLabel.id = "lbl" + task;

        var taskElem = document.createElement("div");
        taskElem.appendChild(taskChkbox);
        taskElem.appendChild(taskLabel);
        taskElem.id = task;

        tasks.appendChild(taskElem);

        taskElem.addEventListener("click", function() {
            loadDetails(tabId, task);
        });

        taskChkbox.addEventListener("click", function() {
            changeCheckState(tabId, task, taskChkbox.checked);
        });
    });

    loadDetails(tabId, Object.keys(tempData[tabId])[0]);
}

function loadDetails(tabId, taskId) {
    document.getElementById("details").innerHTML = "<h2>" + taskId + "</h2><br/>" + tempData[tabId][taskId][1];
}

function changeCheckState(tabId, taskId, checked) {
    socket.emit('checkedTask', orgId, tabId, taskId, checked, username)
}


socket.on('setCheckState', function(dicChange) 
{
    tabId = dicChange["tabId"];
    taskId = dicChange["taskId"];
    checked = dicChange["checked"];
    username = dicChange["username"];
    
    tempData[tabId][taskId][0] = checked;

    if(currentTab == tabId)
    {
        loadTab(tabId);
    }

    if (checked == true)
    {
        $('#chatBody').append('<p>' + username + ' a complété une tâche!</p>');
    }
});


