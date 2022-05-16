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
            <div class="col-12 text-center">
                <h1 class="app-header">To-Do List</h1>
            </div>
        </div>
        <div class="row">
            <div class="col-12 text-center">
                <ul class='to-do-list text-center'>
                    % for task in tasks:
                        <li>
                            <input type="checkbox" class="main-description" id="checkbox">{{task}}
                            <a class='task-remove' href='#'>X</a>
                        </li>
                    % end
                </ul>
            </div>
        </div>
    </div>
</body>
</html>