<form action="">
    <label for="task">Edit Task:</label><br>
    <input type="text" name="task" id="task" value="{{old_task}}" required><br>
    <label for="description">Edit Description:</label><br>
    <textarea name="description" id="description" cols="30" rows="10" >{{description}}</textarea><br>
    <input type="submit" name="save" value="Save" id=""><br>
    <input type="submit" name="delete" value= 'Delete'>
<p><a href="/">Go Home</a></p>

</form>