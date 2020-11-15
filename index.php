<?php 
##################################################
# By Manal Shaikh (github.com/ManalShaikh)
# Design credit AdminLite v3(Google up)
# Sorry not sorry for the messy code. 
# Of course I am not responsible for whatever you do with this. Pls dont do anything illegal or bad. Read the license for more info.
# Credits are more than appreciated in any environment.
##################################################
include("config.php");
include('class/userClass.php');
require 'includes/IndexFuncs.php';
?>
<!DOCTYPE html>
<html>
<head>
<style>
#container{width: 700px}
#login,#signup{width: 300px; border: 1px solid #d6d7da; padding: 0px 15px 15px 15px; border-radius: 5px;font-family: arial; line-height: 16px;color: #333333; font-size: 14px; background: #ffffff;rgba(200,200,200,0.7) 0 4px 10px -1px; align-content: center;}
#login{float:left;}
#signup{float:right;}
h3{color:#365D98}
form label{font-weight: bold;}
form label, form input{display: block;margin-bottom: 5px;width: 90%}
form input{ border: solid 1px #666666;padding: 10px;border: solid 1px #BDC7D8; margin-bottom: 20px}
.button {
    background-color: #5fcf80 !important;
    border-color: #3ac162 !important;
    font-weight: bold;
    padding: 12px 15px;
    max-width: 100px;
    color: #ffffff;
}
.errorMsg{color: #cc0000;margin-bottom: 10px}
</style>
<body>
<center>
<div id="login">
<h3>Login</h3>
<form method="post" action="" name="login">
<label>Username or Email</label>
<input type="text" name="usernameEmail" autocomplete="off" />
<label>Password</label>
<input type="password" name="password" autocomplete="off"/>
<div class="errorMsg"><?php echo $errorMsgLogin; ?></div>
<input type="submit" class="button" name="loginSubmit" value="Login">
</form>
</div>
</center>
</body>
</html>
