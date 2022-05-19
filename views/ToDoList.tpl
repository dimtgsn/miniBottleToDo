<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="stylesheet" href="../static/style.css">
    <title>To-Do List</title>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-12 text-center mb-5">
                <h1 class="app-header">ToDo List</h1>
            </div>
        </div>
        <div class="row">
            <div class="col-12 text-left">
                <ul class='to-do-list'>
                    % for task in tasks:
                        % if task.is_completed:
                            <li class='main-description'>
                                <a class='task-remove' href='api/delete/{{task.uid}}'>
                                    <img src='../static/trashCan.svg' alt="Delete">
                                </a>

                                <label class="custom-checkbox">
                                    <input data-uid={{task.uid}} type="checkbox" disabled="true">
                                    <span>{{task}}</span>
                                </label>
                            </li>
                        % else:
                            <li class='main-description'>
                                <a class='task-remove' href='api/delete/{{task.uid}}'>
                                    <img src='../static/trashCan.svg' alt="Delete">
                                </a>

                                <label class="custom-checkbox">
                                    <input data-uid={{task.uid}} type="checkbox">
                                    <span>{{task}}</span>
                                </label>
                            </li>
                        % end
                    % end
                </ul>
                <form action='/ToDoList/add-task' method='post' id="todo-add" class="mt-3">
                    <button class="add btn" type="submit">+</button>
                    <h2 class='desc-btn'>Add New Task</h2>
                    <input id='new-todo-desc' type="text" placeholder="Add New Task" class="form-control" name='description'/>
                </form>
            </div>
        </div>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
    <script src='../static/script.js'></script>
</body>
</html>