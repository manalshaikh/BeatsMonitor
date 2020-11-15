<?php
##################################################
# By Manal Shaikh (github.com/ManalShaikh)
# Design credit AdminLite v3(Google up)
# Sorry not sorry for the messy code. 
# Of course I am not responsible for whatever you do with this. Pls dont do anything illegal or bad. Read the license for more info.
# Credits are more than appreciated in any environment.
##################################################
if(!empty($_SESSION['uid']))
{
$session_uid=$_SESSION['uid'];
include('class/userClass.php');
$userClass = new userClass();
}

if(empty($session_uid))
{
$url=BASE_URL.'index.php';
header("Location: $url");
}


?>